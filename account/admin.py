# -*- coding: utf-8 -*-

from django.contrib import admin

from account.models import UserProfile, UserFile


admin.site.register(UserProfile)
admin.site.register(UserFile)


