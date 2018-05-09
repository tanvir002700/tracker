from django import template
import datetime

register = template.Library()

@register.filter
def duration(seconds):
    return str(datetime.timedelta(seconds=seconds))
