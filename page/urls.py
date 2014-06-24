# -*- coding: utf-8 -*-
#
# urls.py for app 'page'
#

from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView, RedirectView
from django.core.urlresolvers import reverse_lazy

urlpatterns = patterns('',
    # index page
    url(r'^$', RedirectView.as_view(url=reverse_lazy('index'))),
    # introduction page
    url(r'^introduction/$',
        TemplateView.as_view(template_name='page/introduction.html'),
        name='introduction'),
    # committee page
    url(r'^committee/$',
        TemplateView.as_view(template_name='page/committee.html'),
        name='committee'),
    # sponsor page
    url(r'^sponsor/$',
        TemplateView.as_view(template_name='page/sponsor.html'),
        name='sponsor'),
    # traffic page
    url(r'^traffic/$',
        TemplateView.as_view(template_name='page/traffic.html'),
        name='traffic'),
    # accommodation page
    url(r'^accommodation/$',
        TemplateView.as_view(template_name='page/accommodation.html'),
        name='accommodation'),
    # contact page
    url(r'^contact/$',
        TemplateView.as_view(template_name='page/contact.html'),
        name='contact'),
    # about page
    url(r'^about/$',
        TemplateView.as_view(template_name='page/about.html'),
        name='about'),
)

