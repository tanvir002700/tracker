from django.db import models
from core.models import TimeStampedModel
from accounts.models import User
from django.utils import timezone
from datetime import timedelta


class AttandanceMixing(object):
    pass


class Attandance(TimeStampedModel):
    enter_at = models.DateTimeField(null=True)
    out_at = models.DateTimeField(null=True)
    total_time = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    def is_logged_in(self):
        return self.out_at is None

    def login(self):
        if self.enter_at is None:
            self.enter_at = timezone.now()
            self.save()

    def decorator(original):
        def update_total_time(*args, **kwargs):
            original(*args, **kwargs)
            self = args[0]
            enter_date = self.enter_at.date()
            out_date = self.out_at.date()
            self.total_time = (self.out_at - self.enter_at).total_seconds()
            if enter_date != out_date:
                self.total_time = timedelta(hours=2).total_seconds()
        return update_total_time

    @decorator
    def logout(self):
        if self.out_at is None:
            self.out_at = timezone.now()
            self.save()

