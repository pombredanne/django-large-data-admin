from django.conf.urls.defaults import *

urlpatterns = patterns('large_data_admin.views',
    url(r'^m2m/add/(?P<model_str>[\w._]+)/$', 'add_json'),
    url(r'^m2m/rm/(?P<model_str>[\w._]+)/$', 'rm_json'),
    url(r'^m2m/check/(?P<model_str>[\w._]+)/$', 'check_json'),
    url(r'^m2m/remove/(?P<app>[\w_]+)/(?P<model>[\w_]+)/(?P<field>[\w_]+)/(?P<pk>[\d]+)/', "m2m_remove_view"),

    url(r'^fk/add/(?P<model_str>[\w\._]+)/$', 'fk_add_json'),

    url(r'filter/(?P<model_str>[\w\._]+)/(?P<field>[\w_]+)', "filter_json"),
)
