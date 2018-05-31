from datetime import datetime
from django.test import TestCase

from accounts.models import User
from leave_tracker.models import Leave, Season

class TestMixing(object):
    def setUp(self):
        self.season = Season.objects.create()
        self.user = User.objects.create_user(username='jacob', email='jacob@test.com', password='top_secret')
        self.sick_leave = Leave.objects.create(leave_type=Leave.SICK_LEAVE, leave_reason='test',
                                               date_from=datetime.now(), date_to=datetime.now(),
                                               user_season=self.user.userseason_set.last())
        self.casual_leave = Leave.objects.create(leave_type=Leave.CAUSAL_LEAVE, leave_reason='test',
                                                 date_from=datetime.now(), date_to=datetime.now(),
                                                 user_season=self.user.userseason_set.last())

class LeaveTest(TestMixing, TestCase):
    def test_default_value(self):
        self.assertEqual(self.sick_leave.status, Leave.PENDING)

    def test_leave_type(self):
        self.assertEqual(self.sick_leave.leave_type, Leave.SICK_LEAVE)
        self.assertEqual(self.casual_leave.leave_type, Leave.CAUSAL_LEAVE)
