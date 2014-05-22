from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from store.views import IndexListView, StoreDetailListView

urlpatterns = patterns('',
    url(r'^$', IndexListView.as_view(), name='home'),
    url(r'^store/(?P<pk>\d+)/$', StoreDetailListView.as_view(), name='store_detail'),
    url(r'^admin/', include(admin.site.urls)),
)
