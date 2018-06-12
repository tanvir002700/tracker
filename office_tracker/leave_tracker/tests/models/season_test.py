from django.test import TestCase

from accounts.models import User
from leave_tracker.models import Season

class TestMixing(object):
    def setUp(self):
        self.user = User.objects.create_user(username='jacob', email='jacob@test.com', password='top_secret')

class TestSeason(TestMixing, TestCase):
    def test_post_create_user_season_after_create_season(self):
        season = Season.objects.create()
        self.assertEqual(season.users.count(), 1)
        self.assertEqual(season.id, self.user.season_set.first().id)
