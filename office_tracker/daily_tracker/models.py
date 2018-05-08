from django.db import models
from core.models import TimeStampedModel
from accounts.models import User
from django.utils import timezone
from .decorators import update_total_time


class Attandance(TimeStampedModel):
    enter_at = models.DateTimeField(null=True)
    out_at = models.DateTimeField(null=True)
    total_time = models.DecimalField(default=0, max_digits=19, decimal_places=10)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    def is_logged_in(self):
        return self.out_at is None

    def login(self):
        if self.enter_at is None:
            self.enter_at = timezone.now()
            self.save()

    @update_total_time
    def logout(self):
        if self.out_at is None:
            self.out_at = timezone.now()
            self.save()

