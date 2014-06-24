# -*- coding: utf-8 -*-
#
# utilities to use with app 'archive'
#

from django import template

from archive.models import Archive


register = template.Library()

@register.filter
def get_archive_title(id):
    archive = Archive.objects.get(id=id)
    return archive.title

@register.filter
def get_archive_description(id):
    archive = Archive.objects.get(id=id)
    return archive.description

@register.filter
def get_archive_url(id):
    archive = Archive.objects.get(id=id)
    return archive.file.url

@register.filter
def get_archive_category(id):
    archive = Archive.objects.get(id=id)
    return archive.category.name

