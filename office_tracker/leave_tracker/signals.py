from django.apps import apps

def assign_season_to_all_user(**kwargs):
    instance = kwargs.get('instance')
    User = apps.get_model('accounts', 'User')
    UserSeason = apps.get_model('leave_tracker', 'UserSeason')
    users = User.objects.all()
    user_seasons = []
    for user in users:
        user_seasons.append(UserSeason(user=user, season=instance))
    UserSeason.objects.bulk_create(user_seasons)
