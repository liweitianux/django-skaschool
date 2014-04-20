# -*- coding: utf-8 -*-
#
# urls.py for app 'page'
#

from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView, RedirectView
from django.core.urlresolvers import reverse_lazy

urlpatterns = patterns('',
    # test page
    url(r'^test/$', TemplateView.as_view(template_name='test.html'),
        name='test'),
    # index page
    url(r'^$', RedirectView.as_view(url=reverse_lazy('index'))),
)

