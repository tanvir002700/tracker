from django.test import TestCase
from django.utils import timezone

from accounts.models import User
from daily_tracker.models import Attandance


class TestMixing(object):
    def setUp(self):
        self.user = User.objects.create_user(username='jacob',
                                             email='jacob@test.com',
                                             password='top_secret')
class AttandanceTest(TestMixing, TestCase):
    def test_user_relation(self):
        attandance = Attandance(enter_at=timezone.now(), user=self.user)

        self.assertIsInstance(attandance.user, User)

    def test_is_logged_in_true(self):
        attandance = Attandance(enter_at=timezone.now(), user=self.user)

        self.assertTrue(attandance.is_logged_in())

    def test_is_logged_in_false(self):
        attandance = Attandance(enter_at=timezone.now(), out_at=timezone.now(), user=self.user)

        self.assertFalse(attandance.is_logged_in())

    def test_login_method(self):
        attandance = Attandance()
        attandance.login()

        self.assertTrue(attandance.is_logged_in())

    def test_logout_method(self):
        attandance = Attandance(enter_at=timezone.now())
        attandance.logout()

        self.assertFalse(attandance.is_logged_in())
        self.assertNotEqual(attandance.total_time, 0)
