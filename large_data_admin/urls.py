from django.conf.urls.defaults import *

urlpatterns = patterns('large_data_admin.views',
    url(r'^add/(?P<app>[\w\-]+)/(?P<model>[\w\-]+)/(?P<pk>[\d]+)/(?P<field>[\w\-]+)/$', 'add_json'),
    url(r'^add_process/(?P<app>[\w\-]+)/(?P<model>[\w\-]+)/(?P<pk>[\d]+)/(?P<field>[\w\-]+)/(?P<value>\d+)/$', 'add_process'),
    url(r'^rm_process/(?P<app>[\w\-]+)/(?P<model>[\w\-]+)/(?P<pk>[\d]+)/(?P<field>[\w\-]+)/(?P<value>\d+)/$', 'rm_process'),
    url(r'^rm/(?P<app>[\w\-]+)/(?P<model>[\w\-]+)/(?P<pk>[\d]+)/(?P<field>[\w\-]+)/$', 'rm_json'),
    url(r'^check/(?P<app>[\w\-]+)/(?P<model>[\w\-]+)/(?P<pk>[\d]+)/(?P<field>[\w\-]+)/$', 'check_json'),
    url(r'^selected/(?P<app>[\w\-]+)/(?P<model>[\w\-]+)/(?P<pk>[\d]+)/(?P<field>[\w\-]+)/$', 'selected_json'),

    url(r'^select/add/(?P<app>[\w\-]+)/(?P<model>[\w\-]+)/$', 'select_add_json'),
)
