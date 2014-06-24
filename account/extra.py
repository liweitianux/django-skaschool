# -*- coding: utf-8 -*-

"""
Extra models for app account
"""

from django import forms
from django.db import models
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _

from south.modelsinspector import add_introspection_rules


### custom fields ###
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
                    raise forms.ValidationError(_('Please keep filesize under %(maxsize)s. Current filesize %(filesize)s') % {'maxsize':filesizeformat(self.max_upload_size), 'filesize':filesizeformat(file._size)}, code='invalid')
            else:
                raise forms.ValidationError(_("Unsupported filetype"), code='invalid')
        except AttributeError:
            pass
        #
        return data

## add custom fields to south inspection
add_introspection_rules([
    (
        [ContentTypeRestrictedFileField],   # class these apply to
        [],                                 # positional arguments
        {                                   # keyword argument
            "content_types": ["content_types", {}],
            "max_upload_size": ["max_upload_size", {}],
        },
    ),
], ["^account\.extra\.ContentTypeRestrictedFileField"])


