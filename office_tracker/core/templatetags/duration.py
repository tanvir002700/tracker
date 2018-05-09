from django import template
import datetime

register = template.Library()

@register.filter(name='duration')
def duration(seconds):
    return str(datetime.timedelta(seconds=seconds))
