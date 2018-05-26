import datetime
from django import template

register = template.Library()

@register.filter
def duration(seconds):
    return str(datetime.timedelta(seconds=seconds))
