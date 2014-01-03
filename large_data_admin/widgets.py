from django.forms.widgets import Widget
from django.template import loader
from django.utils.safestring import mark_safe
from django.conf import settings

from helpers import get_model

class ManyToManyWidget(Widget):
    def __init__(self, model_str, search_field, **kwargs):
        self.model_str = model_str
        self.search_field = search_field
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
            "field": self.search_field,
        }))

class SelectWidget(Widget):
    def __init__(self, model_str, search_field, **kwargs):
        self.model_str = model_str
        self.search_field = search_field
        return super(SelectWidget, self).__init__(**kwargs)

    def render(self, name, value, attrs=None):
        if value and value != "None":
            obj = get_model(self.model_str).objects.get(pk=value)
            text_value = "%s #%s" % (getattr(obj, self.search_field), obj.pk)
        else:
            text_value = ""
            value = ""

        return mark_safe(loader.render_to_string("large_data_admin/fk/widget.html", {
            "STATIC_URL": settings.STATIC_URL,
            "name": name,
            "value": value,
            "text_value": text_value,
            "model_str": self.model_str,
            "field": self.search_field,
        }))
