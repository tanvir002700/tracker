import pytz
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin

class TimezoneMiddleware(MiddlewareMixin):
    tzname = None

    def process_request(self, request):
        self.tzname = request.session.get('django_timezone')
        if self.tzname:
            timezone.activate(pytz.timezone(self.tzname))
        else:
            timezone.activate(pytz.timezone('Asia/Dhaka'))

