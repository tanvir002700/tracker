from django.db import models
from django.utils import timezone

from core.models import TimeStampedModel
from accounts.models import User


class Season(TimeStampedModel):
    title = models.TextField()
    total_leave = models.IntegerField(default=0)
    users = models.ManyToManyField(User, through='UserSeason')


class UserSeason(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    season = models.ForeignKey(Season, on_delete=models.PROTECT)

    class Meta(object):
        unique_together = ['user', 'season']


class Leave(TimeStampedModel):
    SICK_LEAVE = 'SK'
    CAUSAL_LEAVE = 'CA'
    LEAVE_TYPE = (
        (SICK_LEAVE, 'Sick Leave'),
        (CAUSAL_LEAVE, 'Causal Leave')
    )

    APPROVED = 'APPROVED'
    PENDING = 'PENDING'
    CANCELED = 'CANCELED'
    STATUS = (
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (CANCELED, 'Canceled')
    )

    leave_type = models.CharField(max_length=3, choices=LEAVE_TYPE, default=SICK_LEAVE)
    leave_reason = models.TextField()
    date_from = models.DateField(default=timezone.now)
    date_to = models.DateField(default=timezone.now)
    status = models.CharField(max_length=15, choices=STATUS, default=PENDING)
    user_season = models.ForeignKey(UserSeason, on_delete=models.CASCADE)

    def __str__(self):
        return self.leave_reason
