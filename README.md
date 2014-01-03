django-large-data-admin
=======================

Admin widgets for managing large data in ForeignKey and ManyToMany and toher.

### Authors
*  Ondrej Sika, <http://ondrejsika.com>, ondrej@ondrejsika.com

### Source
* Python Package Index: <http://pypi.python.org/pypi/django-large-data-admin>
* GitHub: <https://github.com/sikaondrej/django-large-data-admin>

## Documentation

### Instalation

Instalation is very simple over pip.

    # pip install django-large-data-admin

add to `INSTALLED_APPS` in `settings.py`

    INSTALLED_APPS += ("large_data_admin", )

and to root urls in `urls.py`

    urlpatterns += patterns('', url(r'^large_data_admin/', include('large_data_admin.urls')))

### Components

#### Fields
* db_fields.ManyToManyField(RelatedModel)
* db_fields.ForeignKey(RelatedModel, search_fied)

#### Filters
* filters.get_ajax_filter(filter_title, model, field)

### Usage

#### In models.py

``` python
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
```

#### In admin.py

``` python
from django.contrib import admin
from large_data_admin.filters import get_ajax_filter
from models import MyType, MyModel, MyRelatedModel

class MyModelAdmin(admin.ModelAdmin):
    list_filter = (
        get_ajax_filter("type", MyModel, "my_type__name"),
    )
    def lookup_allowed(self, key, val):
        return True


admin.site.register(MyModel, MyModelAdmin)
admin.site.register(MyType)
admin.site.register(MyRelatedModel)
```