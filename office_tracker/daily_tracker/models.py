from django.db import models
from core.models import TimeStampedModel
from accounts.models import User


class Attandance(TimeStampedModel):
    enter_at = models.DateTimeField(null=True)
    out_at = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    def is_logged_in(self):
        return self.out_at is None
