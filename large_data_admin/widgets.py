from django.forms.widgets import Widget

from django.template import loader
from django.utils.safestring import mark_safe
from django.conf import settings

import random

class ManyToManyWidget(Widget):
    is_required = False

    def __init__(self, model_str, **kwargs):
        self.model_str = model_str
        return super(self.__class__, self).__init__(**kwargs)

    def value_from_datadict(self, data, files, name):
        value = data.get(name)
        if value:
            return value.split(',')

    def render(self, name, value, attrs=None):
        if value:
            value = [str(i) for i in value]
        else:
            value = []
        
        return mark_safe(loader.render_to_string("large_data_admin/m2m/widget.html", {
            "STATIC_URL": settings.STATIC_URL,
            "name": name,
            "value": ",".join(value),
            "model_str": self.model_str,
        }))

class SelectWidget(Widget):
    is_required = False

    def __init__(self, model, blank, **kwargs):
        self.model = model
        self.str_model = u"%s.%s"%(model.__module__, model.__name__)
        self.blank = blank
        return super(self.__class__, self).__init__(**kwargs)

    def render(self, name, value, attrs=None, choices=()):
        if value:
            Model = self.model
            text_value = Model.objects.get(pk=value).__unicode__()
        else:
            text_value = ""
        return mark_safe(loader.render_to_string("large_data_admin/select.html", {
            "STATIC_URL": settings.STATIC_URL,
            "selected": value,
            "model": self.str_model,
            "blank": self.blank,
            "field": name,
            "text_value": text_value,
            "prefix": str(random.randint(1000000000, 9999999999)),
        }))