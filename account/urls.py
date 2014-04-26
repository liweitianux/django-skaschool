# -*- coding: utf-8 -*-

"""
urls.py for app 'account'
customize 'registration.backends.default.urls' to use custom form
"""

from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required

from registration.backends.default.views import ActivationView
from registration.backends.default.views import RegistrationView

from account.views import ResendEmailView, ProfileView, UpdateProfileView, ListApprovedView
from account.forms import UserRegForm


urlpatterns = patterns('',
    ## profile
    url(r'^profile/$',
        login_required(ProfileView.as_view()),
        name='profile'),
    # update profile
    url(r'^profile/update/$',
        login_required(UpdateProfileView.as_view()),
        name='profile_update'),
    # update profile done
    url(r'^profile/update/done/$',
        login_required(TemplateView.as_view(template_name='account/profile_update_done.html')),
        name='profile_update_done'),
    # resend activate email
    url(r'^email/resend/$',
        ResendEmailView.as_view(),
        name='email_resend'),
    # resend activate email done
    url(r'^email/resend/done/$',
        TemplateView.as_view(template_name='account/email_resend_done.html'),
        name='email_resend_done'),
    ## show approved user list
    url(r'^list/approved/$', login_required(ListApprovedView.as_view()),
        name='list_approved'),
)

urlpatterns += patterns('django.contrib.auth.views',
    ## django auth views
    # login
    url(r'^login/$', 'login',
        {'template_name': 'account/login.html'},
        name='login'),
    # logout
    url(r'^logout/$', 'logout',
        {'template_name': 'account/logout.html'},
        name='logout'),
    ## change password
    # If 'post_change_redirect' not provided,
    # then redirect to url 'password_change_done'.
    url(r'^password/change/$', 'password_change',
        {'template_name': 'account/password_change.html'},
        name='password_change'),
    # change password done
    url(r'^password/change/done$', 'password_change_done',
        {'template_name': 'account/password_change_done.html'},
        name='password_change_done'),
    ## reset password
    url(r'^password/reset/$', 'password_reset',
        {'template_name': 'account/password_reset_form.html',
         'subject_template_name': 'account/password_reset_subject.txt',
         'email_template_name': 'account/password_reset_email.html',},
        name='password_reset'),
    # reset password done
    url(r'^password/reset/done/$', 'password_reset_done',
        {'template_name': 'account/password_reset_done.html'},
        name='password_reset_done'),
    # reset password confirm
    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'password_reset_confirm',
        {'template_name': 'account/password_reset_confirm.html'},
        name='password_reset_confirm'),
    # reset password complete
    url(r'^password/reset/complete/$', 'password_reset_complete',
        {'template_name': 'account/password_reset_complete.html'},
        name='password_reset_complete'),
)

urlpatterns += patterns('',
    ## django-registration
    # 0. registration_disallowed
    url(r'^register/closed/$',
        TemplateView.as_view(template_name='registration/registration_closed.html'),
        name='registration_disallowed'),
    # 1. registration_register
    url(r'^register/$',
        RegistrationView.as_view(form_class=UserRegForm),
        name='registration_register'),
    # 2. registration_complete
    url(r'^register/complete/$',
        TemplateView.as_view(template_name='registration/registration_complete.html'),
        name='registration_complete'),
    # 4. registration_activation_complete
    url(r'^activate/complete/$',
        TemplateView.as_view(template_name='registration/activation_complete.html'),
        name='registration_activation_complete'),
    # 3. registration_activate (place this section *AFTER* step 4)
    # Activation keys get matched by \w+ instead of the more specific
    # [a-fA-F0-9]{40} because a bad activation key should still get to the view;
    # that way it can return a sensible "invalid key" message instead of a
    # confusing 404.
    url(r'^activate/(?P<activation_key>\w+)/$',
        ActivationView.as_view(),
        name='registration_activate'),
)


