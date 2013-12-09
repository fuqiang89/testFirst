from django.conf.urls import patterns, include, url
from django.contrib import admin
from app.te import current_datetime, real_time, js_get, realtime
from django.conf import settings
import os
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testFirst.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^f/$',current_datetime),
    url(r'^t/$',real_time),
    url(r'jsget/$',js_get),
    url(r'realtime/$',realtime),
)

