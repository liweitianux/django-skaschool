# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.contenttypes import generic

from notice.models import Notice, NoticeCategory, NoticeAttachment


class NoticeAttachmentInline(generic.GenericTabularInline):
    model = NoticeAttachment


class NoticeAdmin(admin.ModelAdmin):
    inlines = [
        NoticeAttachmentInline,
    ]


## register to admin
admin.site.register(Notice, NoticeAdmin)
admin.site.register(NoticeCategory)
admin.site.register(NoticeAttachment)

