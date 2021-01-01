from django import template
from django.utils.safestring import mark_safe
import json

register = template.Library()


# pass django template variables in javascript
# https://stackoverflow.com/questions/298772/django-template-variables-and-javascript
# This template filters converts variable to JSON string.
@register.filter(is_safe=True)
def js(obj):
    return mark_safe(json.dumps(obj))