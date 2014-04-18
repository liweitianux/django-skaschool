# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^page/', include('page.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html'),
        name='index'),
)

## demo
urlpatterns += patterns('',
    url(r'^demo/', include('demo.urls')),
)

## django-registration
urlpatterns += patterns('',
    url(r'^accounts/', include('registration.backends.default.urls')),
)

## staticfiles
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()


