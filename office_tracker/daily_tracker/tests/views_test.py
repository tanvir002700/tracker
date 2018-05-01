from django.urls import reverse
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser

from accounts.models import User
from daily_tracker.views import DailyLoginView


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
    def test_when_user_logged_in(self):
        self.client.login(**self.credentials)
        response = self.client.get(reverse('daily_tracker:login'))

        self.assertRedirects(response, expected_url=reverse('daily_tracker:attandance_list'),
                             status_code=302, target_status_code=200)

    def test_when_user_not_logged_in(self):
        response = self.client.get(reverse('daily_tracker:login'))

        self.assertRedirects(response, expected_url='/accounts/login/?next=/daily_tracker/login/',
                             status_code=302, target_status_code=200)

    def test_multiple_login(self):
        self.client.login(**self.credentials)
        self.client.get(reverse('daily_tracker:login'))

        response = self.client.get(reverse('daily_tracker:login'))
        self.assertEqual(self.user.attandance_set.count(), 1)
