from django.conf.urls import patterns, include, url
from django.contrib import admin
from marketing.views import HomePage
from accounts.views import AccountList
from accounts.urls import account_urls
from contacts.urls import contact_urls
from contacts.views import ContactDelete
from communications.urls import comm_urls
from communications.views import CommDelete


urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', HomePage.as_view(), name="home"),
                       url(r'^signup/$', 'brankocrm.subscribers.views.subscriber_new', name='sub_new'),
                       url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
                       url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login/'}),
                       url(r'^account/new/$', 'brankocrm.accounts.views.account_cru', name='account_new'),
                       url(r'^account/list/$', AccountList.as_view(), name='account_list'),
                       url(r'^account/(?P<uuid>[\w-]+)/', include(account_urls)),
                       url(r'^contact/new/$', 'brankocrm.contacts.views.contact_cru', name='contact_new'),
                       url(r'^contact/(?P<uuid>[\w-]+)/', include(contact_urls)),
                       url(r'^contact/(?P<pk>[\w-]+)/delete/$',ContactDelete.as_view(), name='contact_delete'),
                       url(r'^comm/new/$', 'brankocrm.communications.views.comm_cru', name='comm_new'),
                       url(r'^comm/(?P<uuid>[\w-]+)/', include(comm_urls)),
                       url(r'^comm/(?P<pk>[\w-]+)/delete/$', CommDelete.as_view(), name='comm_delete'),
                       )
