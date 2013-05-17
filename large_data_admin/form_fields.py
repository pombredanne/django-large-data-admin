from django import forms
from django.db.models import get_model

from widgets import ManyToManyWidget

class ModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def __init__(self, app_name, model_name, object_pk=1, initial=None, **kwargs):
        defaults = {
            'widget': ManyToManyWidget(app_name, model_name, object_pk),
        }
        defaults.update(kwargs)
        if not 'queryset' in kwargs:
            queryset = get_model(app_name, model_name).objects.all()
            super(ModelMultipleChoiceField, self).__init__(queryset=queryset, **defaults)
        else:
            super(ModelMultipleChoiceField, self).__init__(initial=initial, **defaults)