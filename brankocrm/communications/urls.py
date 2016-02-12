from django.conf.urls import patterns, url

comm_urls = patterns('',
                     url(r'^$', 'brankocrm.communications.views.comm_detail', name="comm_detail"),
                     url(r'^edit/$', 'brankocrm.communications.views.comm_cru', name='comm_update'),
                     )
