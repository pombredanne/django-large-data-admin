from django import forms
from django.db.models import get_model

from widgets import ManyToManyWidget, SelectWidget

class ModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def __init__(self, model_str, **kwargs):
        super(ModelMultipleChoiceField, self).__init__(widget=ManyToManyWidget(model_str), **kwargs)

class ModelChoiceField(forms.ModelMultipleChoiceField):
    def __init__(self, to, blank, **kwargs):
        defaults = {
            'widget': SelectWidget(to, blank),
        }
        defaults.update(kwargs)
        super(self.__class__, self).__init__(**defaults)