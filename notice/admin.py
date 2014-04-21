# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.contenttypes.generic import GenericTabularInline

from notice.models import Notice, NoticeCategory, NoticeAttachment


class NoticeAttachmentInline(GenericTabularInline):
    model = NoticeAttachment


class NoticeAdmin(admin.ModelAdmin):
    inlines = [
        NoticeAttachmentInline,
    ]


## register to admin
admin.site.register(Notice, NoticeAdmin)
admin.site.register(NoticeCategory)

