from django.db import models
from large_data_admin import db_fields as lda

class MyType(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return u"<MyType: %s>" % self.name

class MyModel(models.Model):
    name = models.CharField(max_length=255)
    my_type = lda.ManyToManyField(MyType, "name")

    def __unicode__(self):
        return u"<MyModel: %s>" % self.name

class MyRelatedModel(models.Model):
    name = models.CharField(max_length=255)
    base_model = lda.ForeignKey(MyModel, "name")

    def __unicode__(self):
        return u"<MyRelatedModel: %s>" % self.name