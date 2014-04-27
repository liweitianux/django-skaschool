# -*- coding: utf-8 -*-

"""
Extra models for app account
"""

from django.db import models
from django import forms
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _

import os


class ContentTypeRestrictedFileField(models.FileField):
    """
    Same as FileField, but you can specify:
        * content_types - list containing allowed content_types.
            Example: ['application/pdf', 'image/jpeg']
        * max_upload_size - a number indicating the maximum file
            size allowed for upload.
            2.5MB - 2621440
            5MB   - 5242880
            10MB  - 10485760
            20MB  - 20971520
            50MB  - 52428800
            100MB - 104857600
            250MB - 214958080
            500MB - 429916160
    """
    def __init__(self, *args, **kwargs):
        self.content_types = kwargs.pop("content_types")
        self.max_upload_size = kwargs.pop("max_upload_size")
        super(ContentTypeRestrictedFileField, self).__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super(ContentTypeRestrictedFileField, self).clean(*args, **kwargs)
        file = data.file
        # check content type and file size
        try:
            content_type = file.content_type
            #print content_type
            #raise forms.ValidationError(_("Invalid filetype."), code='invalid')
            if content_type in self.content_types:
                if file._size > self.max_upload_size:
                    raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (filesizeformat(self.max_upload_size), filesizeformat(file._size)), code='invalid')
            else:
                raise forms.ValidationError(_("Invalid filetype."), code='invalid')
        except AttributeError:
            pass
        #
        return data


### OverwriteStorage ###
class OverwriteStorage(FileSystemStorage):
    """
    overwrite original file before store the new one
    """
    def get_available_name(self, name):
        """
        Returns a filename that's free on the target storage system,
        and available for new content to be written to.
        Ref: http://djangosnippets.org/snippets/976/

        This file storage solves overwrite on upload problem. Another
        proposed solution was to override the save method on the model
        like so (from https://code.djangoproject.com/ticket/11663):

        def save(self, *args, **kwargs):
            try:
                this = MyModelName.objects.get(id=self.id)
                if this.MyImageFieldName != self.MyImageFieldName:
                    this.MyImageFieldName.delete()
            except: pass
            super(MyModelName, self).save(*args, **kwargs)
        """
        # If the filename already exists,
        # remove it as if it was a true file system
        if self.exists(name):
            filepath = os.path.join(settings.MEDIA_ROOT, name)
            if os.path.isfile(filepath):
                os.remove(filepath)
        return name


