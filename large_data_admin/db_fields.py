from django.db import models

import form_fields

class ManyToManyField(models.ManyToManyField):
    def __init__(self, to, app_name, model_name, model_field=None, **kwargs):
        self.app_name = app_name
        self.model_name = model_name
        self.model_field = model_field
        super(self.__class__, self).__init__(to, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': form_fields.ModelMultipleChoiceField,
            'app_name': self.app_name,
            'model_name': self.model_name,
            "model_field": self.model_field,
        }
        defaults.update(kwargs)
        return super(self.__class__, self).formfield(**defaults)