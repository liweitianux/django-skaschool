# -*- coding: utf-8 -*-
#
# urls.py for app 'page'
#

from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy

from archive.views import ArchiveView


urlpatterns = patterns('',
    # notice list view
    url(r'^all$', ArchiveView.as_view(),
        name='archive_all'),
    url(r'^archive/all$',
        RedirectView.as_view(url=reverse_lazy('archive_all'))),
)

