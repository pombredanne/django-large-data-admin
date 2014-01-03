from django import forms
from django.db.models import get_model

from widgets import ManyToManyWidget, SelectWidget

class ModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def __init__(self, model_str, search_field, **kwargs):
        defaults = {
            'widget': ManyToManyWidget(model_str, search_field),
        }
        defaults.update(kwargs)
        super(ModelMultipleChoiceField, self).__init__(**defaults)

class ModelChoiceField(forms.ModelChoiceField):
    def __init__(self, model_str, search_field, **kwargs):
        defaults = {
            'widget': SelectWidget(model_str, search_field),
        }
        defaults.update(kwargs)
        super(ModelChoiceField, self).__init__(**defaults)