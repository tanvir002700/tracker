from django.contrib.auth.models import AbstractUser
from django.db import models
from core.models import TimeStampedModel


class User(AbstractUser, TimeStampedModel):
    date_of_birth = models.DateField(null=True)

