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

add to `INSTALLED_APPS` in your settings.py

    INSTALLED_APPS += ("large_data_admin", )

and to root urls

    urlpatterns += patterns('', url(r'^large_data_admin/', include('large_data_admin.urls')))

### Components

#### Fields
* db_fields.ManyToManyField(RelatedModel)
* db_fields.ForeignKey(RelatedModel, search_fied)

#### Filters
* filters.get_ajax_filter(filter_title, model, field)

### Example of usage

Look at <http://github.com/ondrejsika/lda-example> or 
 [models.py](https://github.com/ondrejsika/lda-example/blob/master/lda_example/models.py) for fields, [admin.py](https://github.com/ondrejsika/lda-example/blob/master/lda_example/admin.py) for filters.