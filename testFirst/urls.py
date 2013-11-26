from django.conf.urls import patterns, include, url
from django.contrib import admin
from app.te import current_datetime
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testFirst.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^f/$',current_datetime),
)
