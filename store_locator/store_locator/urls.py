from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from store.views import IndexListView

urlpatterns = patterns('',
    url(r'^$', IndexListView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
