# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView


urlpatterns = patterns('',
    # admin
    url(r'^admin/', include(admin.site.urls)),
    # index page
    url(r'^$', TemplateView.as_view(template_name='index.html'),
        name='index'),
    # app 'page'
    url(r'^page/', include('page.urls')),
    # app 'notice'
    url(r'^notice/', include('notice.urls')),
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


