from django.apps import AppConfig
from django.db.models.signals import post_save
from django.apps import apps
from .signals import set_user_current_season

class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        User = apps.get_model('accounts', 'User')
        post_save.connect(set_user_current_season, sender=User)
