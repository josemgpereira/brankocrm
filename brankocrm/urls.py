from django.conf.urls import patterns, include, url
from django.contrib import admin
from marketing.views import HomePage

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', HomePage.as_view(), name="home"),
                       )
