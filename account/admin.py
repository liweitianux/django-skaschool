# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _

from account.models import UserProfile, UserFile

import os


class UserProfileAdmin(admin.ModelAdmin):
    """
    customize the admin interface for UserProfile
    """
    actions = [
        'approve_users',
        'sponsor_users',
        'cancel_approve_users',
        'cancel_sponsor_users',
        'reset_approve_users',
        'reset_sponsor_users',
    ]
    list_display = (
        'user',
        'realname',
        'gender',
        'institute',
        'identify',
        'reason',
        'transcript_url',
        'supplement',
        'attachments',
        'is_approved',
        'is_sponsored',
    )

    ## custom admin actions
    def approve_users(self, request, queryset):
        """
        Approve the selected users.
        """
        profiles_updated = queryset.update(is_approved='Y')
        if profiles_updated == 1:
            msg = _("1 user was successfully approved.")
        else:
            msg = _("%(num)s users were successfully approved." % {'num': profiles_updated})
        self.message_user(request, msg)
    approve_users.short_description = _("Approve users")

    def sponsor_users(self, request, queryset):
        """
        Sponsor the selected users.
        """
        profiles_updated = queryset.update(is_sponsored='Y')
        if profiles_updated == 1:
            msg = _("1 user was successfully sponsored.")
        else:
            msg = _("%(num)s users were successfully sponsored." % {'num': profiles_updated})
        self.message_user(request, msg)
    sponsor_users.short_description = _("Sponsor users")

    def cancel_approve_users(self, request, queryset):
        """
        Cancel the approval of the selected users.
        """
        profiles_updated = queryset.update(is_approved='N')
        if profiles_updated == 1:
            msg = _("1 user was successfully cancelled approval.")
        else:
            msg = _("%(num)s users were successfully cancelled approval." % {'num': profiles_updated})
        self.message_user(request, msg)
    cancel_approve_users.short_description = _("Cancel approve users")

    def cancel_sponsor_users(self, request, queryset):
        """
        Cancel the sponsor of the selected users.
        """
        profiles_updated = queryset.update(is_sponsored='N')
        if profiles_updated == 1:
            msg = _("1 user was successfully cancelled sponsor.")
        else:
            msg = _("%(num)s users were successfully cancelled sponsor." % {'num': profiles_updated})
        self.message_user(request, msg)
    cancel_sponsor_users.short_description = _("Cancel sponsor users")

    def reset_approve_users(self, request, queryset):
        """
        Reset the approval of the selected users.
        """
        profiles_updated = queryset.update(is_approved='C')
        if profiles_updated == 1:
            msg = _("1 user was successfully reset approval.")
        else:
            msg = _("%(num)s users were successfully reset approval." % {'num': profiles_updated})
        self.message_user(request, msg)
    reset_approve_users.short_description = _("Reset approve users")

    def reset_sponsor_users(self, request, queryset):
        """
        Reset the sponsor of the selected users.
        """
        profiles_updated = queryset.update(is_sponsored='C')
        if profiles_updated == 1:
            msg = _("1 user was successfully reset sponsor.")
        else:
            msg = _("%(num)s users were successfully reset sponsor." % {'num': profiles_updated})
        self.message_user(request, msg)
    reset_sponsor_users.short_description = _("Reset sponsor users")

    ## custom fields
    def transcript_url(self, obj):
        """
        return the html code of transcript with url link
        """
        transcript = obj.transcript
        if transcript:
            html = '<a href="%(url)s">%(name)s</a>' % {
                'url': transcript.url,
                'name': os.path.basename(transcript.name),
            }
        else:
            html = _("Null")
        return format_html(html)
    transcript_url.short_description = _("Transcript")

    def attachments(self, obj):
        """
        return the html code of attachments with url
        """
        user = obj.user
        files = user.userfile_set.all()
        if files:
            attachments = ['<a href="%(url)s">%(name)s</a>' % {
                    'url': userfile.file.url,
                    'name': os.path.basename(userfile.file.name),
                }
                for userfile in files
            ]
            html = '<br>'.join(attachments)
        else:
            html = _("Null")
        return format_html(html)
    attachments.short_description = _("Attachments")


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserFile)


