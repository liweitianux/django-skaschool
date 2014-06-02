# -*- coding: utf-8 -*-

from django.contrib import admin
from django.conf.urls import url
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse

from account.models import UserProfile, UserFile

from account.csv_unicode import UnicodeReader, UnicodeWriter

import os
import datetime
import csv


class UserProfileAdmin(admin.ModelAdmin):
    """
    customize the admin interface for UserProfile
    """
    actions = [
        'approve_users',
        'cancel_approve_users',
        'reset_approve_users',
        'sponsor_users',
        'cancel_sponsor_users',
        'reset_sponsor_users',
        'users_checkin',
        'users_not_checkin',
        'users_checkin_reset',
    ]
    list_display = (
        'user',
        'email',
        'realname',
        'gender',
        'institute',
        'identity',
        'reason',
        'transcript_url',
        'supplement',
        'attachments',
        'is_approved',
        'is_sponsored',
        'is_checkin',
    )
    # search fields
    search_fields = [
        'user__username',
        'user__email',
        'realname',
        'institute',
    ]

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

    # control 'is_checkin' field
    def users_checkin(self, request, queryset):
        """
        Mark selected users as checked in.
        """
        profiles_updated = queryset.update(is_checkin='Y')
        if profiles_updated == 1:
            msg = _("1 user was successfully marked as checkin.")
        else:
            msg = _("%(num)s users were successfully marked as checkin." % {'num': profiles_updated})
        self.message_user(request, msg)
    users_checkin.short_description = _("Mark users as checked in")

    def users_not_checkin(self, request, queryset):
        """
        Mark selected users as NOT checked in.
        """
        profiles_updated = queryset.update(is_checkin='N')
        if profiles_updated == 1:
            msg = _("1 user was marked as not checkin.")
        else:
            msg = _("%(num)s users were marked as not checkin." % {'num': profiles_updated})
        self.message_user(request, msg)
    users_not_checkin.short_description = _("Mark users as not checked in")

    def users_checkin_reset(self, request, queryset):
        """
        Reset checkin status of selected users.
        """
        profiles_updated = queryset.update(is_checkin='X')
        if profiles_updated == 1:
            msg = _("1 user was reset status of checkin.")
        else:
            msg = _("%(num)s users were reset status of checkin." % {'num': profiles_updated})
        self.message_user(request, msg)
    users_checkin_reset.short_description = _("Reset users checkin status")

    ## custom fields
    def email(self, obj):
        """
        return the email of the user profile
        """
        user = obj.user
        return user.email
    email.short_description = _("E-mail")

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

    ## added a view to display all userprofile info (csv format)
    def get_urls(self):
        urls = super(type(self), self).get_urls()
        my_urls = [
            url(r'^csv/$', self.userprofile_csv_view,
                name='userprofile_csv_view'),
        ]
        return my_urls + urls

    def userprofile_csv_view(self, request):
        """
        custom admin view to display all userprofile info in csv format
        """
        userprofile_objs = UserProfile.objects.all()
        fieldnames = userprofile_objs[0].dump_fieldnames()
        fields = [k for k,v in fieldnames.items()]
#        # header
#        header = u''
#        for k in fields:
#            header += u'{0},'.format(fieldnames[k])
#        header += '\n'
#        # contents
#        contents = u''
#        for obj in userprofile_objs:
#            data = obj.dump()
#            cline = u''
#            for k in fields:
#                if k == 'attachments':
#                    cline += u'{0},'.format('||'.join(data[k]))
#                else:
#                    cline += u'{0},'.format(data[k])
#            cline += '\n'
#            contents += cline
#        return HttpResponse(header+contents, content_type='text/plain')
        filename = '{0}-{1}.csv'.format('registration', datetime.date.today().strftime('%Y%m%d'))
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="{0}"'.format(filename)
        # Python 2's csv module does not support unicode I/O
        #writer = csv.writer(response)
        writer = UnicodeWriter(response)
        # header
        header = []
        for k in fields:
            header.append(fieldnames[k])
        writer.writerow(header)
        # contents
        for obj in userprofile_objs:
            data = obj.dump()
            row = []
            for k in fields:
                if k == 'attachments':
                    row.append(';'.join(data[k]))
                else:
                    row.append(unicode(data[k]))
            writer.writerow(row)
        #
        return response


###
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserFile)


