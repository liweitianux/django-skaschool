# -*- coding: utf-8 -*-

from django.db import models
from django.db.models.signals import pre_delete
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _

from tools.storage import OverwriteStorage, file_cleanup


class Notice(models.Model):
    """
    model 'Notice' to record and display notice
    """
    title = models.CharField(_("Title"), max_length=100)
    pubtime = models.DateTimeField(_("Publish time"), auto_now_add=True)
    category = models.ForeignKey('NoticeCategory', verbose_name=_("Category"))
    is_important = models.BooleanField(_("Is important"), default=False)
    contents = models.TextField(_("Contents"),
            help_text=_("Markdown syntax supported"))
    # NoticeAttachment to deal with attachments
    attachments = generic.GenericRelation('NoticeAttachment')

    class Meta:
        verbose_name = _('notice')
        verbose_name_plural = _('notices')
        ordering = ['-pubtime', 'id']

    def __unicode__(self):
        return u'Notice %s: %s' % (self.category.category_name, self.title)

    def show_pubtime(self):
        # used in 'list_notice.html' template
        return self.pubtime.strftime('%Y-%m-%d')


class NoticeCategory(models.Model):
    """
    model 'NoticeCategory' to provide category selections for 'Notice'
    """
    category_name = models.CharField(_("Category name"), max_length=100)
    created_time = models.DateTimeField(_("Created time"), auto_now_add=True)

    class Meta:
        verbose_name = _('notice category')
        verbose_name_plural = _('notice categories')

    def __unicode__(self):
        return u'NoticeCategory : %s' % self.category_name


class NoticeAttachment(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    description = models.TextField(_("Description"), blank=True)
    attachment = models.FileField(upload_to='notice/attachments',
            verbose_name=_("Attachment"),
            storage=OverwriteStorage())
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey("content_type", "object_id")

    class Meta:
        verbose_name = _('notice attachment')
        verbose_name_plural = _('notice attachments')


### connect to signal and sender
pre_delete.connect(file_cleanup, sender=NoticeAttachment)


