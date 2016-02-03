from django.conf.urls import patterns, include, url
from django.contrib import admin
from marketing.views import HomePage

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', HomePage.as_view(), name="home"),
                       url(r'^signup/$', 'brankocrm.subscribers.views.subscriber_new', name='sub_new'),
                       url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
                       url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login/'}),
                       )
