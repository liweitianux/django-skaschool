# -*- coding: utf-8 -*-

"""
account/forms.py for skaschool
"""

from django import forms
from registration.forms import RegistrationFormUniqueEmail
from django.utils.translation import ugettext_lazy as _

from account.models import UserProfile


class UserRegForm(RegistrationFormUniqueEmail):
    """
    based on 'django-registration' RegistrationFormUniqueEmail
    add fields 'realname', 'gender', 'institute' and 'captcha'
    """
    # XXX: keep consistent with GENDERS in 'models.UserProfile'
    GENDERS = (
        ('M', _("Male")),
        ('F', _("Female")),
        ('X', _("Secret")),
    )
    realname = forms.CharField(max_length=30, label=_("Name"))
    gender = forms.ChoiceField(choices=GENDERS, label=_("Gender"))
    institute = forms.CharField(max_length=100, label=_("Institute"))

    def __init__(self, *args, **kw):
        super(UserRegForm, self).__init__(*args, **kw)
        # order form fields
        self.fields.keyOrder = [
                'username',
                'email',
                'password1',
                'password2',
                'realname',
                'gender',
                'institute',
        ]


class UpdateProfileForm(forms.ModelForm):
    """
    ModelForm of 'UserProfile' used in 'UpdateProfileView'
    """
    # extra email field
    email = forms.EmailField(label=_("E-mail"))

    class Meta:
        model = UserProfile
        fields = ('realname', 'gender', 'institute')


