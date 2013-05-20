from django import forms
from django.db.models import get_model

from widgets import ManyToManyWidget, SelectWidget

class ModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def __init__(self, app_name, model_name, model_field=None, object_pk=None, initial=None, **kwargs):
        defaults = {
            'widget': ManyToManyWidget(app_name, model_name, model_field, object_pk),
        }
        defaults.update(kwargs)
        if not 'queryset' in kwargs:
            queryset = get_model(app_name, model_name).objects.all()
            super(ModelMultipleChoiceField, self).__init__(queryset=queryset, **defaults)
        else:
            super(ModelMultipleChoiceField, self).__init__(initial=initial, **defaults)

class ModelChoiceField(forms.ModelChoiceField):
    def __init__(self, to, **kwargs):
        defaults = {
            'widget': SelectWidget(to),
        }
        defaults.update(kwargs)
        super(self.__class__, self).__init__(**defaults)