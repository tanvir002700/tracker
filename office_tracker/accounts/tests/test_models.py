from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser

from accounts.models import User
from daily_tracker.models import Attandance
from django.utils import timezone

class UserMixing(object):
    def create_user(self, username='test', email='test@email.com', password='top_secret'):
        return User.objects.create(username=username, email=email, password=password)

    def create_attandance_without_logout(user):
        user = create_user()
        return user.attandance_set.create(enter_at=timezone.now())

    def create_attandance_with_logout(user):
        user = create_user()
        return user.attandance_set.create(enter_at=timezone.now(), out_at=timezone.now())

class UserModelTest(UserMixing, TestCase):
    def test_user_create(self):
        u = self.create_user()
        self.assertTrue(isinstance(u, User))

