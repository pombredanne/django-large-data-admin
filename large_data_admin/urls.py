from django.conf.urls import *

urlpatterns = patterns('large_data_admin.views',
    url(r'^get/$', 'get_json'),

    url(r'^m2m/remove/(?P<model_str>[\w_\.]+)/', "m2m_remove_view"),
    url(r'^m2m/list/(?P<model_str>[\w_\.]+)/', "m2m_list_view"),
)
