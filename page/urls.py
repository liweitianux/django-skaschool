# -*- coding: utf-8 -*-
#
# urls.py for app 'page'
#

from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView

urlpatterns = patterns('',
    url(r'^test/$', TemplateView.as_view(template_name='test.html'),
        name='test'),
)

