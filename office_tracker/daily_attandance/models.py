from django.db import models
from core.models import TimeStampedModel
from accounts.models import User


class Attandance(TimeStampedModel):
    enter_at = models.DateTimeField(null=False)
    out_at = models.DateTimeField(null=True)
