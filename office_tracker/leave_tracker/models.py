from django.db import models
from django.utils import timezone

class Leave(models.Model):
    SICK_LEAVE = 'SK'
    CAUSAL_LEAVE = 'CA'
    LEAVE_TYPE = (
        (SICK_LEAVE, 'Sick Leave'),
        (CAUSAL_LEAVE, 'Causal Leave')
    )

    leave_type = models.CharField(max_length=3, choices=LEAVE_TYPE, default=SICK_LEAVE)
    leave_reason = models.TextField()
    date_from = models.DateField(default=timezone.now)
    date_to = models.DateField(default=timezone.now)

    def __str__(self):
        return self.leave_reason
