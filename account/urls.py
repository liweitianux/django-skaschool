# -*- coding: utf-8 -*-

"""
urls.py for app 'account'
customize 'registration.backends.default.urls' to use custom form
"""

from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView

from registration.backends.default.views import ActivationView
from registration.backends.default.views import RegistrationView

from account.forms import UserRegForm


urlpatterns = patterns('',
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
    ## django auth views
    # login
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'account/login.html'},
        name='login'),
    # logout
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'account/logout.html'},
        name='logout'),
    # profile
    url(r'^profile/$',
        TemplateView.as_view(template_name='account/profile.html'),
        name='profile'),
)


