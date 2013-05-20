from django.forms.widgets import Widget

from django.template import loader
from django.utils.safestring import mark_safe
from django.conf import settings
from django.db.models import get_model

import random

class ManyToManyWidget(Widget):
    is_required = False

    def __init__(self, app_name=None, model_name=None, model_field=None, object_pk=None, **kwargs):
        self.app_name = app_name
        self.model_name = model_name
        self.object_pk = object_pk
        self.model_field = model_field
        return super(self.__class__, self).__init__(**kwargs)

    def render(self, name, value, attrs=None, choices=()):
        field = self.model_field or name
        return mark_safe(loader.render_to_string("large_data_admin/widget.html", {
            "STATIC_URL": settings.STATIC_URL,
            "selected": value,
            "app": self.app_name,
            "model": self.model_name,
            "pk": self.object_pk,
            "field": field,
            "prefix": str(random.randint(1000000000, 9999999999)),
        }))

class SelectWidget(Widget):
    is_required = False

    def __init__(self, model, **kwargs):
        self.model = model
        self.app_name = model.__module__.split(".")[0] # XXX
        return super(self.__class__, self).__init__(**kwargs)

    def render(self, name, value, attrs=None, choices=()):
        if value:
            Model = get_model(self.app_name, self.model.__name__)
            text_value = Model.objects.get(pk=value).__unicode__()
        else:
            text_value = ""
        return mark_safe(loader.render_to_string("large_data_admin/select.html", {
            "STATIC_URL": settings.STATIC_URL,
            "selected": value,
            "app": self.app_name,
            "model": self.model.__name__,
            "field": name,
            "text_value": text_value,
            "prefix": str(random.randint(1000000000, 9999999999)),
        }))