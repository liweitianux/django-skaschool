# -*- coding: utf-8 -*-
#
# app 'account' models
# registration
#

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

from django.utils.translation import ugettext_lazy as _

from registration.signals import user_registered


class UserProfile(models.Model):
    """
    custom user profile
    connected with signal 'user_registered' sent by 'django-registration'
    """
    # XXX: keep consistent with GENDERS in 'forms.UserRegForm'
    GENDERS = (
        ('M', _("Male")),
        ('F', _("Female")),
        ('X', _("Secret")),
    )
    user = models.ForeignKey(User, unique=True, verbose_name=_("Username"))
    realname = models.CharField(_("Name"), max_length=30)
    gender = models.CharField(_("Gender"), max_length=1, choices=GENDERS)
    institute = models.CharField(_("Institute"), max_length=100)
    # store the infomation about approval and sponsorship
    is_approved = models.BooleanField(_("Is approved"), default=False)
    is_sponsored = models.BooleanField(_("Is sponsored"), default=False)

    class Meta:
        verbose_name = _('user profile')
        verbose_name_plural = _('user profiles')

    def __unicode__(self):
        return u'UserProfile for %s' % self.user


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
    profile.save()

### connect 'user_registered_callback' to signal
user_registered.connect(user_registered_callback)


### add to adim
admin.site.register([
    UserProfile,
])


