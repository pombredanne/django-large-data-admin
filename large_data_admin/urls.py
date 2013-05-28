from django.conf.urls.defaults import *

urlpatterns = patterns('large_data_admin.views',
    url(r'^m2m/add/(?P<model_str>[\w._]+)/$', 'add_json'),
    url(r'^m2m/rm/(?P<model_str>[\w._]+)/$', 'rm_json'),
    url(r'^m2m/check/(?P<model_str>[\w._]+)/$', 'check_json'),

    url(r'^many-to-many/list/add/(?P<app>[\w\-]+)/(?P<model>[\w\-]+)/(?P<pk>[\d]+)/(?P<field>[\w\-]+)/$', 'many_to_namy_list_add_view'),
    url(r'^many-to-many/list/rm/(?P<app>[\w\-]+)/(?P<model>[\w\-]+)/(?P<pk>[\d]+)/(?P<field>[\w\-]+)/$', 'many_to_namy_list_rm_view'),

    url(r'^select/add/(?P<model>[\w\-.]+)/$', 'select_add_json'),
)
