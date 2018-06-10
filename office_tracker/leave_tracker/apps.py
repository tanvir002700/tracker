from django.apps import AppConfig
from django.db.models.signals import post_save
from .signals import test_signals

class LeaveTrackerConfig(AppConfig):
    name = 'leave_tracker'

    def ready(self):
        from .models import Season
        print("execute ready")
        post_save.connect(test_signals, sender=Season)
