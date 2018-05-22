from django.urls import reverse
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser
from datetime import datetime

from accounts.models import User
from leave_tracker.models import Leave
from leave_tracker.views import LeaveListView


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


class TestLeaveListView(TestMixing, TestCase):
    def test_unauthorized_access(self):
        response = self.client.get(reverse('leave_tracker:leave_list'))
        self.assertRedirects(response, expected_url='/accounts/login/?next=/leave_tracker/', status_code=302, target_status_code=200)

    def test_authorize_access(self):
        self.client.login(**self.credentials)
        self.client.get(reverse('daily_tracker:login'))

        response = self.client.get(reverse('leave_tracker:leave_list'))
        self.assertTrue(response.status_code, 200)


class TestLeaveDetailView(TestCase):
    pass


class TestLeaveCreateView(TestCase):
    pass


class TestLeaveUpdateView(TestCase):
    pass


class TestLeaveDeleteView(TestCase):
    pass
