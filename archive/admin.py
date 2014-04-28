# -*- coding: utf-8 -*-

from django.contrib import admin

from archive.models import Archive, ArchiveCategory


## register to admin
admin.site.register(Archive)
admin.site.register(ArchiveCategory)

