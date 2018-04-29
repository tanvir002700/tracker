from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser

from accounts.models import User


class AccountsTest(TestCase):

    def create_user(self, username='test', email='test@email.com', password='top_secret'):
        return User.objects.create(username=username, email=email, password=password)

    def test_user_create(self):
        u = self.create_user()
        self.assertTrue(isinstance(u, User))
