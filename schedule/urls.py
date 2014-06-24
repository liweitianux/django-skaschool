# -*- coding: utf-8 -*-
#
# urls.py for app 'page'
#

from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView

from schedule.views import ScheduleView


urlpatterns = patterns('',
    # program page
    url(r'^all/$',
        ScheduleView.as_view(),
        name='schedule_all'),
)

