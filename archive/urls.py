# -*- coding: utf-8 -*-
#
# urls.py for app 'page'
#

from django.conf.urls import patterns, include, url

from archive.views import ArchiveView


urlpatterns = patterns('',
    # notice list view
    url(r'^archive/all$', ArchiveView.as_view(),
        name='archive_all'),
)

