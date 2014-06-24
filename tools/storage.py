# -*- coding: utf-8 -*-
#
# custom storage class
# and storage related tools
#

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db.models.fields.files import FieldFile

import os


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


### delete files associated with model FileField
# Pre-delete signal function for deleting files a model
# https://djangosnippets.org/snippets/2820/
def file_cleanup(sender, instance, *args, **kwargs):
    """
    Deletes the file(s) associated with a model instance. The model
    is not saved after deletion of the file(s) since this is meant
    to be used with the pre_delete signal.
    """
    for field_name, _ in instance.__dict__.iteritems():
        field = getattr(instance, field_name)
        if (issubclass(field.__class__, FieldFile) and field.name):
            # pass False so FileField does not save the model
            field.delete(save=False)

