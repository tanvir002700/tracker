from django.apps import AppConfig


class LeaveTrackerConfig(AppConfig):
    name = 'leave_tracker'

    def ready(self):
        print("execute ready")
