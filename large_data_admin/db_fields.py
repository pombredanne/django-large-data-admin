from django.db import models

import form_fields

class ManyToManyField(models.ManyToManyField):
    def __init__(self, to, **kwargs):
        self.model_str = u"%s.%s"%(to.__module__, to.__name__)
        super(self.__class__, self).__init__(to, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': form_fields.ModelMultipleChoiceField,
            "model_str": self.model_str,
        }
        defaults.update(kwargs)
        return super(self.__class__, self).formfield(**defaults)

class ForeignKey(models.ForeignKey):
    def __init__(self, to, **kwargs):
        self.model_str = u"%s.%s"%(to.__module__, to.__name__)
        super(ForeignKey, self).__init__(to, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': form_fields.ModelChoiceField,
            "model_str": self.model_str,
        }
        defaults.update(kwargs)
        return super(ForeignKey, self).formfield(**defaults)