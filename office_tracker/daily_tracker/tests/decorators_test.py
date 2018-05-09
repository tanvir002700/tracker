from django.test import TestCase
from daily_tracker.decorators import update_total_time
from daily_tracker.models import Attandance
from django.utils import timezone
from datetime import timedelta

class TestDecorators(TestCase):
    def test(self):
        attandance = Attandance.objects.create(enter_at=timezone.now(), out_at=timezone.now() + timedelta(hours=2))
        @update_total_time
        def mock(attandance):
            return True

        mock(attandance)
        attandance.refresh_from_db()
        self.assertNotEqual(attandance.total_time, 0)

