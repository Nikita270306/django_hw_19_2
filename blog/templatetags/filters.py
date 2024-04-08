from django import template
from django.conf import settings

register = template.Library()


@register.filter
def mymedia(value):
    if value:
        return f'{settings.MEDIA_URL}{value}'
    return value