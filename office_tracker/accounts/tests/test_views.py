from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser

from accounts.models import User
from accounts.views import AccountDetailView, LoginView


class SimpleTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='jacob', email='jacob@test.com', password='top_secret')

    def test_login(self):
        request = self.factory.get('/accounts/login')
        request.user = AnonymousUser

        response = LoginView.as_view()(request)
        self.assertEqual(response.status_code, 302)

    def test_details(self):
        request = self.factory.get('/accounts/detail')
        request.user = self.user

        response = AccountDetailView.as_view()(request)
        self.assertEqual(response.status_code, 200)
