# -*- coding: utf-8 -*-
#
# app 'account' models
# registration
#

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db.models.fields.files import FieldFile
from django.utils.translation import ugettext_lazy as _

from django.db.models.signals import pre_delete
from registration.signals import user_registered, user_activated

from account.extra import ContentTypeRestrictedFileField, OverwriteStorage

import os


###### account models ######
class UserProfile(models.Model):
    """
    custom user profile
    connected with signal 'user_registered' sent by 'django-registration'
    NOTE: keep this model fields consistent with 'user_registered_callback'
    """
    GENDERS = (
        ('M', _("Male")),
        ('F', _("Female")),
        ('X', _("Secret")),
    )
    # status choices of is_approved
    APPROVED_STATUS = (
        ('Y', _("Yes")),
        ('N', _("No")),
        ('C', _("Checking")),
    )
    # status choices of is_sponsored
    SPONSORED_STATUS = (
        ('Y', _("Yes")),
        ('N', _("No")),
        ('C', _("Checking")),
    )
    # choices for identify
    IDENTIFIES = (
        ('OT', _("Other")),
        ('UG', _("Undergraudate (junior and below)")),
        ('U4', _("Undergraudate (senior)")),
        ('MG', _("Master graudate")),
        ('PG', _("PhD graudate")),
        ('PD', _("Post-doctoral")),
        ('SR', _("Assistant researcher")),
        ('AR', _("Associate researcher")),
        ('DR', _("Distinguished researcher")),
        ('RE', _("Researcher")),
        ('IN', _("Instructor")),
        ('SP', _("Assistant professor")),
        ('AP', _("Associate professor")),
        ('PR', _("Professor")),
    )
    # model fields
    # FK default backward manager name 'userprofile_set'
    user = models.ForeignKey(User, unique=True, verbose_name=_("User"))
    realname = models.CharField(_("Name"), max_length=30)
    gender = models.CharField(_("Gender"), max_length=1, choices=GENDERS)
    institute = models.CharField(_("Institute"), max_length=100)
    identify = models.CharField(_("Identify"), max_length=2,
            choices=IDENTIFIES)
    # reasons to participate
    reason = models.TextField(_("Why attend"))
    # transcript: needed if undergraudate (junior and below)
    transcript = ContentTypeRestrictedFileField(upload_to=lambda instance, filename: u'account/{0}/{1}'.format(instance.user.username, filename),
            verbose_name=_("Transcript"), blank=True, null=True,
            storage=OverwriteStorage(),
            content_types=settings.ALLOWED_CONTENT_TYPES,
            max_upload_size=settings.ALLOWED_MAX_UPLOAD_SIZE)
    # supplement: record additional information
    supplement = models.TextField(_("Supplement"), blank=True)
    # store the infomation about approval and sponsorship
    is_approved = models.CharField(_("Is approved"), max_length=1,
            choices=APPROVED_STATUS, default='C')
    is_sponsored = models.CharField(_("Is sponsored"), max_length=1,
            choices=SPONSORED_STATUS, default='C')

    class Meta:
        verbose_name = _('user profile')
        verbose_name_plural = _('user profiles')

    def __unicode__(self):
        return u'UserProfile for %s' % self.user.username

    def save(self, *args, **kwargs):
        """
        overwrite the original save method to delete old file
        """
        if not self.pk:
            # -> create
            return super(UserProfile, self).save(*args, **kwargs)
        # already exists -> edit
        old_obj = type(self).objects.get(pk=self.pk)
        result = super(UserProfile, self).save(*args, **kwargs)
        # if the path is the same, the file is overwritten already
        if old_obj.transcript.name:
            # old_obj has transcript file
            if not self.transcript.name:
                # new object has no transcript
                old_obj.transcript.delete(save=False)
            elif old_obj.transcript.path != self.transcript.path:
                # new object has transcript file, and differ from old_obj
                old_obj.transcript.delete(save=False)
        #
        return result

    def is_transcript_required(self):
        """
        if 'identify' is UG (undergraduate junior and below); then
        transcript is required, return True. Otherwise, return False
        """
        if (self.identify == 'UG'):
            return True
        else:
            return False

    def get_transcript_filename(self):
        # return the base filename of transcript FileField
        return os.path.basename(self.transcript.name)

    def get_approved(self, *args, **kwargs):
        """
        return list of approved object
        """
        return self.objects.filter(is_approved='Y')

    def get_sponsored(self, *args, **kwargs):
        """
        return list of sponsored object
        """
        return self.objects.filter(is_sponsored='Y')

    def get_gender_value(self):
        """
        return the corresponding value of user's gender
        """
        genders_dict = dict((k, v) for k, v in self.GENDERS)
        return genders_dict.get(self.gender)

    def get_approved_value(self):
        """
        return the corresponding value of is_approved for the user
        """
        approved_dict = dict((k, v) for k, v in self.APPROVED_STATUS)
        return approved_dict.get(self.is_approved)

    def get_sponsored_value(self):
        """
        return the corresponding value of is_sponsored for the user
        """
        sponsored_dict = dict((k, v) for k, v in self.SPONSORED_STATUS)
        return sponsored_dict.get(self.is_sponsored)

    def get_identify_value(self):
        """
        return the corresponding value of identify for the user
        """
        identifies_dict = dict((k, v) for k, v in self.IDENTIFIES)
        return identifies_dict.get(self.identify)

    def get_userfiles(self):
        """
        return the UserFile objects related to this user
        NOTE: transcript is not included here.
        """
        return self.user.userfile_set.all()


class UserFile(models.Model):
    """
    model to deal with user uploaded files
    """
    user = models.ForeignKey(User, verbose_name=_("User"))
    title = models.CharField(_("Title"), max_length=100)
    description = models.TextField(_("Description"), blank=True)
    file = ContentTypeRestrictedFileField(upload_to=lambda instance, filename: u'account/{0}/{1}'.format(instance.user.username, filename),
            verbose_name=_("File"),
            storage = OverwriteStorage(),
            content_types=settings.ALLOWED_CONTENT_TYPES,
            max_upload_size=settings.ALLOWED_MAX_UPLOAD_SIZE)
    created_at = models.DateTimeField(_("Created time"),
            auto_now_add=True)
    modified_at = models.DateTimeField(_("Modified time"), auto_now=True)

    class Meta:
        verbose_name = _('user file')
        verbose_name_plural = _('user files')
        ordering = ['user', 'id']

    def __unicode__(self):
        return u'UserFile of %s: %s' % (self.user.username, self.title)

    def save(self, *args, **kwargs):
        """
        overwrite the original save method to delete old file
        """
        if not self.pk:
            # -> create
            return super(UserFile, self).save(*args, **kwargs)
        # already exists -> edit
        old_obj = type(self).objects.get(pk=self.pk)
        result = super(UserFile, self).save(*args, **kwargs)
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


###### signal callback ######
def user_registered_callback(sender, user, request, **kwargs):
    """
    callback of signal 'user_registered' from 'django-registration'
    to create custom user profile
    ref: http://johnparsons.net/index.php/2013/06/28/creating-profiles-with-django-registration/
    """
    profile = UserProfile(user = user)
    profile.realname = request.POST['realname']
    profile.gender = request.POST['gender']
    profile.institute = request.POST['institute']
    profile.identify = request.POST['identify']
    profile.save()

### connect 'user_registered_callback' to signal user_registered
user_registered.connect(user_registered_callback)

### login user after activated
def login_on_activation(sender, user, request, **kwargs):
    """
    Logs in the user after activation
    """
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, user)

# connect 'login_on_activation' to signal user_activated
user_activated.connect(login_on_activation)


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

### connect to signal and sender
pre_delete.connect(file_cleanup, sender=UserProfile)
pre_delete.connect(file_cleanup, sender=UserFile)


