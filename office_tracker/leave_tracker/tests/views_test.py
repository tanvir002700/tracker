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
        self.sick_leave = Leave.objects.create(leave_type=Leave.SICK_LEAVE, leave_reason='test',
                                          date_from=datetime.now(), date_to=datetime.now())


class TestLeaveListView(TestMixing, TestCase):
    def test_unauthorized_access(self):
        response = self.client.get(reverse('leave_tracker:leave_list'))
        self.assertRedirects(response, expected_url='/accounts/login/?next=/leave_tracker/',
                             status_code=302, target_status_code=200)

    def test_authorize_access(self):
        self.client.login(**self.credentials)
        self.client.get(reverse('daily_tracker:login'))

        response = self.client.get(reverse('leave_tracker:leave_list'))
        self.assertTrue(response.status_code, 200)

    def test_template_used(self):
        self.client.login(**self.credentials)
        self.client.get(reverse('daily_tracker:login'))

        response = self.client.get(reverse('leave_tracker:leave_list'))
        self.assertTemplateUsed(response,'leave_tracker/leave_list.html')



class TestLeaveDetailView(TestMixing, TestCase):
    def test_unauthorized_access(self):
        response = self.client.get(reverse('leave_tracker:detail', kwargs={'pk': self.sick_leave.id}))
        self.assertRedirects(response, expected_url='/accounts/login/?next=/leave_tracker/' + str(self.sick_leave.id),
                             status_code=302, target_status_code=200)

    def test_authorize_access(self):
        self.client.login(**self.credentials)
        self.client.get(reverse('daily_tracker:login'))

        response = self.client.get(reverse('leave_tracker:detail', kwargs={'pk': self.sick_leave.id}))
        self.assertTrue(response.status_code, 200)

    def test_template_used(self):
        self.client.login(**self.credentials)
        self.client.get(reverse('daily_tracker:login'))

        response = self.client.get(reverse('leave_tracker:detail', kwargs={'pk': self.sick_leave.id}))
        self.assertTemplateUsed(response,'leave_tracker/leave_detail.html')


class TestLeaveCreateView(TestMixing, TestCase):
    def test_unauthorized_access(self):
        response = self.client.get(reverse('leave_tracker:create'))
        self.assertRedirects(response, expected_url='/accounts/login/?next=/leave_tracker/create/',
                             status_code=302, target_status_code=200)

    def test_authorize_access(self):
        self.client.login(**self.credentials)

        response = self.client.get(reverse('leave_tracker:create'))
        self.assertTrue(response.status_code, 200)
    def test_get(self):
        self.client.login(**self.credentials)

        response = self.client.get(reverse('leave_tracker:create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'csrfmiddlewaretoken')

class TestLeaveUpdateView(TestCase):
    pass


class TestLeaveDeleteView(TestCase):
    pass
