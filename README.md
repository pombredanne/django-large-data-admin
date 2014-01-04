django-large-data-admin
=======================

Admin widgets for managing large data in ForeignKey and ManyToMany and toher.


* __Authors__: [Ondrej Sika](http://ondrejsika.com/c.html)
* __Python Package Index__: <http://pypi.python.org/pypi/django-large-data-admin>
* __GitHub__: <https://github.com/sikaondrej/django-large-data-admin>

## Documentation

### Try Online

Try on <http://lda.examples.h4y.cz/> with username __test__ and password __test__.

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

### Examples

Example project is in [example_project](example_project) directory, [models.py](example_project/lda_example/models.py) for fields, [admin.py](example_project/lda_example/admin.py) for filters.