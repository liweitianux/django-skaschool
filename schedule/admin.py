# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.contenttypes import generic

from schedule.models import Event, EventAttachment


class EventAttachmentInline(generic.GenericTabularInline):
    model = EventAttachment

class EventAdmin(admin.ModelAdmin):
    inlines = [
        EventAttachmentInline,
    ]


# Register models to admin
admin.site.register(Event, EventAdmin)
admin.site.register(EventAttachment)

