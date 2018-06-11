from django.apps import AppConfig
from django.db.models.signals import post_save
from django.apps import apps
from .signals import assign_season_to_all_user

class LeaveTrackerConfig(AppConfig):
    name = 'leave_tracker'

    def ready(self):
        Season = apps.get_model('leave_tracker', 'Season')
        post_save.connect(assign_season_to_all_user, sender=Season)
