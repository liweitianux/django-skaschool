# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView

from page.views import IndexView


urlpatterns = patterns('',
    # admin
    url(r'^admin/', include(admin.site.urls)),
    # index page
    url(r'^$', IndexView.as_view(), name='index'),
    # app 'page'
    url(r'^page/', include('page.urls')),
    # app 'schedule'
    url(r'^schedule/', include('schedule.urls')),
    # app 'notice'
    url(r'^notice/', include('notice.urls')),
    # app 'archive'
    url(r'^archive/', include('archive.urls')),
)

## django-registration
urlpatterns += patterns('',
    # url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/', include('account.urls')),
)


## staticfiles
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


