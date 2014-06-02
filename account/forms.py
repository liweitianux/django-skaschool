# -*- coding: utf-8 -*-

"""
account/forms.py for skaschool
"""

from django import forms
from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User
from django.contrib.sites.models import Site, RequestSite
from django.utils.translation import ugettext_lazy as _

from registration.forms import RegistrationFormUniqueEmail
from captcha.fields import ReCaptchaField

from account.models import UserProfile, UserFile


class UserRegForm(RegistrationFormUniqueEmail):
    """
    based on 'django-registration' RegistrationFormUniqueEmail
    add fields 'realname', 'gender', 'institute' and 'captcha'
    """
    GENDERS = UserProfile.GENDERS
    IDENTITIES = UserProfile.IDENTITIES
    realname = forms.CharField(max_length=30, label=_("Name"))
    gender = forms.ChoiceField(choices=GENDERS, label=_("Gender"))
    institute = forms.CharField(max_length=100, label=_("Institute (and major)"))
    identity = forms.ChoiceField(choices=IDENTITIES, label=_("Identity"))
    captcha = ReCaptchaField(label=_("Captcha"),
            attrs={'theme': 'clean'})

    #def __init__(self, *args, **kw):
    #    super(UserRegForm, self).__init__(*args, **kw)
    #    # order form fields
    #    self.fields.keyOrder = [
    #            'username',
    #            'email',
    #            'password1',
    #            'password2',
    #            'realname',
    #            'gender',
    #            'institute',
    #            'identity',
    #    ]


class ResendEmailForm(forms.Form):
    """
    form used in ResendEmailView
    """
    username = forms.RegexField(regex=r'^[\w.@+-]+$',
                                max_length=30,
                                label=_("Username"),
                                error_messages={'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")})
    is_update_email = forms.BooleanField(label=_("Is update email"),
            required=False, initial=False)
    email = forms.EmailField(label=_("E-mail"), required=False)

    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        user = User.objects.filter(username=username)
        if not user:
            raise forms.ValidationError(_("Username not exists"), code='invalid')
        return username

    def clean(self):
        # if 'is_update_email' True, then email field is required
        is_update_email = self.cleaned_data.get('is_update_email', False)
        email = self.cleaned_data.get('email', '')
        if (is_update_email and (not email)):
            raise forms.ValidationError(_("Email is required"), code='required')
        return self.cleaned_data

    def update_email(self):
        # update User email if user provided a different email
        username = self.cleaned_data.get('username', '')
        email = self.cleaned_data.get('email', '')
        user = User.objects.get(username=username)
        if email:
            user.email = email
            user.save()

    def resend_email(self):
        # resend activation email
        if Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(self.request)

        username = self.cleaned_data.get('username', '')
        user = User.objects.get(username=username)
        regprofile = user.registrationprofile_set.get(user=user)
        if not regprofile.activation_key_expired():
            regprofile.send_activation_email(site)


class UpdateProfileForm(forms.ModelForm):
    """
    ModelForm of 'UserProfile' used in 'UpdateProfileView'
    """
    # extra email field
    email = forms.EmailField(label=_("E-mail"))

    class Meta:
        model = UserProfile
        fields = (
            'user',
            'realname',
            'gender',
            'institute',
            'identity',
            'reason',
            'transcript',
            'supplement',
        )
        widgets = {
            'user': forms.HiddenInput,
        }

    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        # reorder fields, append 'email' just after 'realname'
        self.fields.keyOrder = [
            'user',
            'realname',
            'email',
            'gender',
            'institute',
            'identity',
            'reason',
            'transcript',
            'supplement',
        ]

    def clean(self):
        """
        check if 'transcript' is needed and provided
        """
        form_data = self.cleaned_data
        user = form_data.get('user')
        profile = user.userprofile_set.get(user=user)
        profile.identity = form_data.get('identity', profile.identity)
        transcript = self.cleaned_data.get('transcript', False)
        if (profile.is_transcript_required() and (not transcript)):
            raise forms.ValidationError(_("Transcript is required."), code='required')
        # not save 'profile' here
        return self.cleaned_data


class UserFileForm(forms.ModelForm):
    """
    form of UserFile, empty_permitted=True
    """
    class Meta:
        model = UserFile

    def __init__(self, *args, **kwargs):
        super(UserFileForm, self).__init__(*args, **kwargs)
        self.empty_permitted = True


### formset ###
# UserFileFormSet: parent_model -> User
UserFileFormSet = inlineformset_factory(User,
        UserFile, form=UserFileForm,
        extra=1, can_delete=True)

