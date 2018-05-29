from datetime import datetime
from django.urls import reverse
from django.test import TestCase, RequestFactory
from django.contrib.messages import get_messages

from accounts.models import User
from leave_tracker.models import Leave


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
        self.assertTemplateUsed(response, 'leave_tracker/leave_list.html')



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
        self.assertTemplateUsed(response, 'leave_tracker/leave_detail.html')


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

        response = self.client.post(reverse('leave_tracker:create'),
                                    {
                                        'leave_type': Leave.SICK_LEAVE,
                                        'leave_reason': 'test',
                                        'date_from': datetime.now().date(),
                                        'date_to': datetime.now().date(),
                                        'status': Leave.APPROVED
                                    }
                                   )
        self.assertTrue(response.status_code, 200)
        self.assertEqual(Leave.objects.count(), 2)
        self.assertEqual(Leave.objects.last().status, Leave.PENDING)


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

    def test_post(self):
        casual_leave = Leave.objects.create(leave_type=Leave.CAUSAL_LEAVE, leave_reason='test',
                                            date_from=datetime.now(), date_to=datetime.now())
        self.client.login(**self.credentials)

        response = self.client.post(reverse('leave_tracker:update', kwargs={'pk': casual_leave.id}),
                                    {
                                        'leave_type': 'SK',
                                        'leave_reason': 'update',
                                        'date_from': datetime.now().date(),
                                        'date_to': datetime.now().date()
                                    }
                                   )

        casual_leave.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(casual_leave.leave_reason, 'update')
        self.assertEqual(casual_leave.leave_type, 'SK')
        self.assertEqual(str(messages[0]), 'successfully update')

    def test_approved_leave_prevent_update(self):
        casual_leave = Leave.objects.create(leave_type=Leave.CAUSAL_LEAVE, leave_reason='test',
                                            date_from=datetime.now().date(), date_to=datetime.now().date(),
                                            status=Leave.APPROVED)
        self.client.login(**self.credentials)

        response = self.client.post(reverse('leave_tracker:update', kwargs={'pk': casual_leave.id}),
                                    {
                                        'leave_type': 'SK',
                                        'leave_reason': 'update',
                                        'date_from': datetime.now().date(),
                                        'date_to': datetime.now().date()
                                    }
                                   )

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'cant update')
        self.assertEqual(response.status_code, 302)

    def test_cancled_leave_prevent_update(self):
        casual_leave = Leave.objects.create(leave_type=Leave.CAUSAL_LEAVE, leave_reason='test',
                                            date_from=datetime.now().date(), date_to=datetime.now().date(),
                                            status=Leave.CANCELED)
        self.client.login(**self.credentials)

        response = self.client.post(reverse('leave_tracker:update', kwargs={'pk': casual_leave.id}),
                                    {
                                        'leave_type': 'SK',
                                        'leave_reason': 'update',
                                        'date_from': datetime.now().date(),
                                        'date_to': datetime.now().date()
                                    }
                                   )

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'cant update')
        self.assertEqual(response.status_code, 302)



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

    def test_post(self):
        self.client.login(**self.credentials)

        response = self.client.post(reverse('leave_tracker:delete', kwargs={'pk': self.sick_leave.id}))
        self.assertRedirects(response, reverse('leave_tracker:leave_list'), status_code=302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'successfully update')

    def test_approved_leave_prevent_delete(self):
        casual_leave = Leave.objects.create(leave_type=Leave.CAUSAL_LEAVE, leave_reason='test',
                                            date_from=datetime.now(), date_to=datetime.now(), status=Leave.APPROVED)

        self.client.login(**self.credentials)

        response = self.client.get(reverse('leave_tracker:delete', kwargs={'pk': casual_leave.id}))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'cant update')
        self.assertEqual(response.status_code, 302)

    def test_canceled_leave_prevent_delete(self):
        casual_leave = Leave.objects.create(leave_type=Leave.CAUSAL_LEAVE, leave_reason='test',
                                            date_from=datetime.now(), date_to=datetime.now(), status=Leave.CANCELED)

        self.client.login(**self.credentials)

        response = self.client.get(reverse('leave_tracker:delete', kwargs={'pk': casual_leave.id}))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'cant update')
        self.assertEqual(response.status_code, 302)
