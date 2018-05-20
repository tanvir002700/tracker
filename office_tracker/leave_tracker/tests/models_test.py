from django.test import TestCase
from datetime import datetime

from leave_tracker.models import Leave

class TestMixing(object):
    def setUp(self):
        self.sick_leave = Leave.objects.create(leave_type=Leave.SICK_LEAVE, leave_reason='test',
                                                     date_from=datetime.now(), date_to=datetime.now())

class LeaveTest(TestMixing, TestCase):
    def test_default_value(self):
        self.assertEqual(self.sick_leave.status, Leave.PENDING)
