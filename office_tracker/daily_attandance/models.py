from django.db import models
from core.models import TimeStampedModel


class Attandance(TimeStampedModel):
    enter_at = models.DateTimeField(null=False)
    out_at = models.DateTimeField(null=False)

