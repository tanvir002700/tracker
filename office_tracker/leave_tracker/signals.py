from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Season

@receiver(post_save, sender=Season)
def test_signals(sender, **kwargs):
    print("test signals...............")
