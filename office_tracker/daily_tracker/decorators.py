from datetime import timedelta
from django.utils import timezone

def update_total_time(original):
    def wrapper(*args, **kwargs):
        original(*args, **kwargs)
        self = args[0]
        enter_date = timezone.localtime(self.enter_at).date()
        out_date = timezone.localtime(self.out_at).date()
        self.total_time = (self.out_at - self.enter_at).total_seconds()
        if enter_date != out_date:
            self.total_time = timedelta(hours=2).total_seconds()
        self.save()
    return wrapper
