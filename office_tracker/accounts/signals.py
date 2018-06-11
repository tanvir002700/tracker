from django.apps import apps

def set_user_current_season(sender, **kwargs):
    instance = kwargs.get('instance')
    current_season = apps.get_model('leave_tracker', 'Season').objects.last()
    UserSeason = apps.get_model('leave_tracker', 'UserSeason')
    current_user_season = instance.userseason_set.last()
    if current_season and current_user_season is None:
        UserSeason.objects.create(user=instance, season=current_season)
