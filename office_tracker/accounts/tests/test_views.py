from django.urls import reverse
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser

from accounts.models import User
from accounts.views import AccountDetailView, LoginView


class SimpleTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='jacob', email='jacob@test.com', password='top_secret')
        self.credentials = {
            'username': 'jacob',
            'password': 'top_secret'
        }

    def test_registration_get(self):
        response = self.client.get(reverse('accounts:registration'))
        self.assertEqual(response.status_code, 200)

    def test_registration_post(self):
        response = self.client.post(reverse('accounts:registration'), {
            'username': 'test',
            'email': 'test@email.com',
            'password1': '$password_1234',
            'password2': '$password_1234',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 2)

    def test_login_get(self):
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)

    def test_login_post(self):
        response = self.client.post(reverse('accounts:login'), **self.credentials, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_details(self):
        request = self.factory.get('/accounts/detail')
        request.user = self.user

        response = AccountDetailView.as_view()(request)
        self.assertEqual(response.status_code, 200)

