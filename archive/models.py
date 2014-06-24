# -*- coding: utf-8 -*-

from django.db import models
from django.db.models.signals import pre_delete
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from tools.storage import OverwriteStorage, file_cleanup


class Archive(models.Model):
    """
    model 'Archive' to record uploaded files and provide downloads
    """
    title = models.CharField(_("Title"), max_length=100)
    pubtime = models.DateTimeField(_("Publish time"), auto_now_add=True)
    category = models.ForeignKey('ArchiveCategory', verbose_name=_("Category"))
    publisher = models.ForeignKey(User, verbose_name=_("Publisher"))
    description = models.TextField(_("Description"))
    file = models.FileField(verbose_name=_("File"),
            upload_to=lambda instance, filename: u'archive/cat{0}/{1}'.format(instance.category.id, filename),
            storage=OverwriteStorage())

    class Meta:
        verbose_name = _('archive')
        verbose_name_plural = _('archives')
        ordering = ['category', '-pubtime', 'id']

    def __unicode__(self):
        return u'Archive #%s: (%s) %s' % (
                self.id, self.category.name, self.title)

    def show_pubtime(self):
        # used in 'list_notice.html' template
        return self.pubtime.strftime('%Y-%m-%d')

    def save(self, *args, **kwargs):
        """
        overwrite the original save method to delete old file
        """
        if not self.pk:
            # -> create
            return super(type(self), self).save(*args, **kwargs)
        # already exists -> edit
        old_obj = type(self).objects.get(pk=self.pk)
        result = super(type(self), self).save(*args, **kwargs)
        # if the path is the same, the file is overwritten already
        if old_obj.file.name:
            # old_obj has file
            if not self.file.name:
                # new object has no file
                old_obj.file.delete(save=False)
            elif old_obj.file.path != self.file.path:
                # new object has file, and differ from old_obj
                old_obj.file.delete(save=False)
        #
        return result


class ArchiveCategory(models.Model):
    """
    model 'NoticeCategory' to provide category selections for 'Notice'
    """
    name = models.CharField(_("Category name"), max_length=100)
    created_at = models.DateTimeField(_("Created time"), auto_now_add=True)

    class Meta:
        verbose_name = _('archive category')
        verbose_name_plural = _('archive categories')

    def __unicode__(self):
        return u'ArchiveCategory: %s' % self.name


### connect to signal and sender
pre_delete.connect(file_cleanup, sender=Archive)

