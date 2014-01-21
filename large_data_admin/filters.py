import random
import json, urllib

from django.conf import settings
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

def get_ajax_filter(filter_title, model, field, filter_query={}, exclude_query={}):
    class AjaxFilter(admin.SimpleListFilter):
        parameter_name = 'decade'
        title = _(filter_title)
        template = "large_data_admin/filter/ajax_filter.html"
        def __init__(self, *args, **kwargs):
            self.random = "a%s" % random.randint(11111111, 99999999)
            self.STATIC_URL = settings.STATIC_URL
            self.model = "%s.%s" % (model.__module__, model.__name__)
            self.field = field
            self.filter_query  = urllib.quote(json.dumps(filter_query))
            self.exclude_query = urllib.quote(json.dumps(exclude_query))
            super(AjaxFilter, self).__init__(*args, **kwargs)
        def has_output(self):
            return True
        def lookups(self, request, model_admin):
            pass
        def queryset(self, request, queryset):
            pass
    return AjaxFilter
