from django import forms
from django.db.models import get_model

from widgets import ManyToManyWidget, SelectWidget

class ModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def __init__(self, model_str, **kwargs):
        super(ModelMultipleChoiceField, self).__init__(widget=ManyToManyWidget(model_str), **kwargs)

class ModelChoiceField(forms.ModelChoiceField):
    def __init__(self, model_str, **kwargs):
        super(ModelChoiceField, self).__init__(widget=SelectWidget(model_str), **kwargs)