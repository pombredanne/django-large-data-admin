from django.db import models

import form_fields

class ManyToManyField(models.ManyToManyField):
    def __init__(self, to, search_field, **kwargs):
        self.model_str = u"%s.%s"%(to.__module__, to.__name__)
        self.search_field = search_field
        super(ManyToManyField, self).__init__(to, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': form_fields.ModelMultipleChoiceField,
            "model_str": self.model_str,
            "search_field": self.search_field,
        }
        defaults.update(kwargs)
        return super(ManyToManyField, self).formfield(**defaults)

    def south_field_triple(self):
        from south.modelsinspector import introspector
        field_class = "django.db.models.ManyToManyField"
        args, kwargs = introspector(self)
        return (field_class, args, kwargs)

class ForeignKey(models.ForeignKey):
    def __init__(self, to, search_field, **kwargs):
        self.model_str = u"%s.%s"%(to.__module__, to.__name__)
        self.search_field = search_field
        super(ForeignKey, self).__init__(to, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': form_fields.ModelChoiceField,
            "model_str": self.model_str,
            "search_field": self.search_field,
        }
        defaults.update(kwargs)
        return super(ForeignKey, self).formfield(**defaults)

    def south_field_triple(self):
        from south.modelsinspector import introspector
        field_class = "django.db.models.ForeignKey"
        args, kwargs = introspector(self)
        return (field_class, args, kwargs)

class OneToOneField(models.OneToOneField):
    def __init__(self, to, search_field, **kwargs):
        self.model_str = u"%s.%s"%(to.__module__, to.__name__)
        self.search_field = search_field
        super(OneToOneField, self).__init__(to, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': form_fields.ModelChoiceField,
            "model_str": self.model_str,
            "search_field": self.search_field,
        }
        defaults.update(kwargs)
        return super(OneToOneField, self).formfield(**defaults)

    def south_field_triple(self):
        from south.modelsinspector import introspector
        field_class = "django.db.models.OneToOneField"
        args, kwargs = introspector(self)
        return (field_class, args, kwargs)
