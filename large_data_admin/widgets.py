from django.forms.widgets import Widget

from django.template import loader
from django.utils.safestring import mark_safe
from django.conf import settings

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
        return mark_safe(loader.render_to_string("large_data_admin/widget.html", {
            "STATIC_URL": settings.STATIC_URL,
            "selected": value,
            "app": self.app_name,
            "model": self.model_name,
            "pk": self.object_pk,
            "field": self.model_field or name,
            "prefix": str(random.randint(1000000000, 9999999999)),
        }))