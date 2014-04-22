# -*- coding: utf-8 -*-
#
# urls.py for app 'page'
#

from django.conf.urls import patterns, include, url

from notice.views import ListNoticeView


urlpatterns = patterns('',
    # notice list view
    url(r'^list/$', ListNoticeView.as_view(),
        name='list_notice'),
)

