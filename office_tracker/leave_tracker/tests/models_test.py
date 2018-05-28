from datetime import datetime
from django.test import TestCase

from leave_tracker.models import Leave

class TestMixing(object):
    def setUp(self):
        self.sick_leave = Leave.objects.create(leave_type=Leave.SICK_LEAVE, leave_reason='test',
                                               date_from=datetime.now(), date_to=datetime.now())
        self.casual_leave = Leave.objects.create(leave_type=Leave.CAUSAL_LEAVE, leave_reason='test',
                                                 date_from=datetime.now(), date_to=datetime.now())

class LeaveTest(TestMixing, TestCase):
    def test_default_value(self):
        self.assertEqual(self.sick_leave.status, Leave.PENDING)

    def test_leave_type(self):
        self.assertEqual(self.sick_leave.leave_type, Leave.SICK_LEAVE)
        self.assertEqual(self.casual_leave.leave_type, Leave.CAUSAL_LEAVE)
