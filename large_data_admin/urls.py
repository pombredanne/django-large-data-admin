from django.conf.urls.defaults import *

urlpatterns = patterns('large_data_admin.views',
    url(r'^m2m/add/(?P<model_str>[\w._]+)/$', 'add_json'),
    url(r'^m2m/rm/(?P<model_str>[\w._]+)/$', 'rm_json'),
    url(r'^m2m/check/(?P<model_str>[\w._]+)/$', 'check_json'),
    url(r'^m2m/remove/(?P<model_str>[\w_\.]+)/', "m2m_remove_view"),
    url(r'^m2m/list/(?P<model_str>[\w_\.]+)/', "m2m_list_view"),

    url(r'^get/$', 'get_json'),
)
