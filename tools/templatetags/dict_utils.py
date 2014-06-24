# -*- coding: utf-8 -*-
#
# utilities to deal with dictionary in template
#

from django import template


register = template.Library()

@register.filter
def dictkey(d, key):
    try:
        value = d[key]
    except KeyError:
        from django.conf import settings
        value = settings.TEMPLATE_STRING_IF_INVALID
    return value

