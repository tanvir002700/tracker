from django.urls import reverse
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser
from django.utils import timezone

from accounts.models import User
from daily_tracker.views import DailyLoginView, AttandanceListView


class TestMixing(object):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='jacob',
                                             email='jacob@test.com',
                                             password='top_secret')
        self.credentials = {
            'username': 'jacob',
            'password': 'top_secret'
        }


class DailyLoginViewTest(TestMixing, TestCase):
    def test_authorize_access(self):
        self.client.login(**self.credentials)
        response = self.client.get(reverse('daily_tracker:login'))

        self.assertRedirects(response, expected_url=reverse('daily_tracker:attandance_list'),
                             status_code=302, target_status_code=200)

    def test_unauthorized_access(self):
        response = self.client.get(reverse('daily_tracker:login'))

        self.assertRedirects(response, expected_url='/accounts/login/?next=/daily_tracker/login/',
                             status_code=302, target_status_code=200)

    def test_multiple_login(self):
        self.client.login(**self.credentials)
        self.client.get(reverse('daily_tracker:login'))

        response = self.client.get(reverse('daily_tracker:login'))
        self.assertEqual(self.user.attandance_set.count(), 1)


class DailyLogoutViewTest(TestMixing, TestCase):
    def test_authorize_access(self):
        self.user.attandance_set.create(enter_at=timezone.now())
        self.client.login(**self.credentials)

        response = self.client.get(reverse('daily_tracker:logout'))
        self.assertFalse(self.user.is_active_login())

    def test_unauthorized_access(self):
        response = self.client.get(reverse('daily_tracker:logout'))

        self.assertRedirects(response, expected_url='/accounts/login/?next=/daily_tracker/logout/',
                             status_code=302, target_status_code=200)


class AttandanceListViewTest(TestMixing, TestCase):
    def test_one_entry(self):
        request = self.factory.get('/daily_tracker/attandance_list')
        request.user = self.user
        attandance = self.user.attandance_set.create(enter_at=timezone.now())

        response = AttandanceListView.as_view()(request)
        self.assertEqual(response.status_code, 200)
