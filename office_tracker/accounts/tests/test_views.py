from django.urls import reverse
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser

from accounts.models import User
from accounts.views import AccountDetailView, AccountUpdateView

class TestMixing(object):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='jacob', email='jacob@test.com', password='top_secret')
        self.credentials = {
            'username': 'jacob',
            'password': 'top_secret'
        }


class RegisterViewTest(TestCase):
    def test_registration_get(self):
        response = self.client.get(reverse('accounts:registration'))
        self.assertEqual(response.status_code, 200)

    def test_registration_post(self):
        response = self.client.post(reverse('accounts:registration'), {
            'username': 'test',
            'email': 'test@email.com',
            'password1': '$password_1234',
            'password2': '$password_1234',
        }, follow=True)
        self.assertRedirects(response, expected_url='/accounts/login/?next=/accounts/detail/',
                             status_code=302, target_status_code=200)
        self.assertEqual(User.objects.count(), 1)

class LoginViewTest(TestMixing, TestCase):

    def test_get(self):
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        response = self.client.post(reverse('accounts:login'), **self.credentials, follow=True)
        self.assertEqual(response.status_code, 200)


class LogoutViewTest(TestMixing, TestCase):
    def test_logout(self):
        self.client.login(**self.credentials)

        response = self.client.get(reverse('accounts:logout'))
        self.assertRedirects(response, expected_url=reverse('accounts:login'), status_code=302, target_status_code=200)


class DetailViewTest(TestMixing, TestCase):
    def test_details(self):
        request = self.factory.get('/accounts/detail')
        request.user = self.user

        response = AccountDetailView.as_view()(request)
        self.assertEqual(response.status_code, 200)


class UpdateViewTest(TestMixing, TestCase):
    def test_update_get(self):
        request = self.factory.get('/accounts/update')
        request.user = self.user

        response = AccountUpdateView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_update_post(self):
        self.client.login(**self.credentials)

        response = self.client.post(reverse('accounts:update'), {
            'first_name': 'change',
            'last_name': 'change',
            'email': 'email@email.com'
        })
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'change')
        self.assertEqual(self.user.last_name, 'change')
        self.assertEqual(self.user.email, 'email@email.com')
        self.assertRedirects(response, expected_url=reverse('accounts:detail'), status_code=302, target_status_code=200)

