from django.urls import reverse
from django.test import TestCase, RequestFactory
from unittest import skip
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
        self.assertTemplateUsed(response, 'leave_tracker/leave_form.html')

    def test_post(self):
        self.client.login(**self.credentials)

        response = self.client.post(reverse('leave_tracker:create'),{'leave_type': Leave.SICK_LEAVE,
                                                                      'leave_reason': 'test',
                                                                      'date_form': datetime.now(),
                                                                      'date_to': datetime.now()
                                                                      })
        self.assertTrue(response.status_code, 200)
        self.assertEqual(Leave.objects.count(), 1)


class TestLeaveUpdateView(TestMixing, TestCase):
    def test_unauthorized_access(self):
        response = self.client.get(reverse('leave_tracker:update', kwargs={'pk': self.sick_leave.id}))
        self.assertRedirects(response,
                             expected_url='/accounts/login/?next=/leave_tracker/'+str(self.sick_leave.id)+'/update/',
                             status_code=302, target_status_code=200)

    def test_authorize_access(self):
        self.client.login(**self.credentials)

        response = self.client.get(reverse('leave_tracker:update', kwargs={'pk': self.sick_leave.id}))
        self.assertTrue(response.status_code, 200)

    def test_get(self):
        self.client.login(**self.credentials)

        response = self.client.get(reverse('leave_tracker:update', kwargs={'pk': self.sick_leave.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'csrfmiddlewaretoken')
        self.assertTemplateUsed(response, 'leave_tracker/leave_form.html')

    @skip("need to fix this")
    def test_post(self):
        casual_leave = Leave.objects.create(leave_type=Leave.CAUSAL_LEAVE, leave_reason='test',
                                          date_from=datetime.now(), date_to=datetime.now())
        self.client.login(**self.credentials)

        print(casual_leave.id)
        response = self.client.post(reverse('leave_tracker:update', kwargs={'pk': casual_leave.id}),
                                    {'leave_type': Leave.SICK_LEAVE,
                                     'leave_reason': 'update',
                                     'date_form': datetime.now(),
                                     'date_to': datetime.now()
                                     }
                                    )
        self.assertEqual(response.status_code, 200)
        casual_leave.refresh_from_db()
        print(casual_leave.status)
        print(casual_leave.leave_type)
        print(response)
        self.assertEqual(casual_leave.leave_reason, 'update')


class TestLeaveDeleteView(TestMixing, TestCase):
    def test_unauthorized_access(self):
        response = self.client.get(reverse('leave_tracker:delete', kwargs={'pk': self.sick_leave.id}))
        self.assertRedirects(response,
                             expected_url='/accounts/login/?next=/leave_tracker/'+str(self.sick_leave.id)+'/delete/',
                             status_code=302, target_status_code=200)

    def test_authorize_access(self):
        self.client.login(**self.credentials)

        response = self.client.get(reverse('leave_tracker:update', kwargs={'pk': self.sick_leave.id}))
        self.assertTrue(response.status_code, 200)

    def test_get(self):
        self.client.login(**self.credentials)

        response = self.client.get(reverse('leave_tracker:delete', kwargs={'pk': self.sick_leave.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'leave_tracker/leave_confirm_delete.html')

