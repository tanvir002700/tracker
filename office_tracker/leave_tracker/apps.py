from django.apps import AppConfig
from django.db.models.signals import post_save


class LeaveTrackerConfig(AppConfig):
    name = 'leave_tracker'

    def ready(self):
        print("execute ready")
        import leave_tracker.signals
