# -*- coding: utf-8 -*-
#
# models of app 'schedule'
#

from django.db import models
from django.db.models.signals import pre_delete
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _

from tools.storage import OverwriteStorage, file_cleanup


class Event(models.Model):
    """
    model 'Event' to store event information
    and arrange these events to make schedule
    """
    title = models.CharField(_("Title"), max_length=100)
    person = models.CharField(_("Person in charge"), max_length=50)
    date = models.DateField(_("Date"))
    time_start = models.TimeField(_("Start time"))
    time_end = models.TimeField(_("End time"))
    contents = models.TextField(_("Contents"), blank=True,
            help_text=_("Markdown syntax supported"))
    attachments = generic.GenericRelation('EventAttachment')

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")
        ordering = ['date', 'time_start']

    def __unicode__(self):
        return u'Event: %(date)s %(time_start)s-%(time_end)s, %(person)s, %(title)s' % {
                'date': self.date.isoformat(),
                'time_start': self.time_start.strftime('%H:%M'),
                'time_end': self.time_end.strftime('%H:%M'),
                'person': self.person,
                'title': self.title,
        }

class EventAttachment(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    description = models.TextField(_("Description"), blank=True)
    attachment = models.FileField(upload_to='schedule/attachments',
            verbose_name=_("Attachment"),
            storage=OverwriteStorage())
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey("content_type", "object_id")

    class Meta:
        verbose_name = _('Event attachment')
        verbose_name_plural = _('Event attachments')


### connect to signal and sender
pre_delete.connect(file_cleanup, sender=EventAttachment)


