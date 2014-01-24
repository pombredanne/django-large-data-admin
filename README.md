django-large-data-admin
=======================

Admin widgets for managing large data in ForeignKey and ManyToMany and toher.


* __Authors__: [Ondrej Sika](http://ondrejsika.com/c.html), Petr Cermak
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
* filters.get_ajax_filter(filter_title, model, field, filter_query={}, exclude_query={})

If filter_query and exclude_query are empty dictionaries implicit filter is created from model and field attributes:

    Model.objects.filter(field_icontains=input_value)

If filter_query or exclude_query are present no implicit filter is added to query.

If you need concatenate results from filtering by more fields you can type more field names to field attribute and divide them by comma. See examples.

You can use patterns FIELD_NAME and INPUT_VALUE in filter_query and exclude_query dictionaries. They will be filled during filter calling with field and input values.

### Examples

Example project is in [example_project](example_project) directory, [models.py](example_project/lda_example/models.py) for fields, [admin.py](example_project/lda_example/admin.py) for filters.

These example calls of get_ajax_filter are equal:

    get_ajax_filter('Name', User, 'username')
    get_ajax_filter('Name', User, 'username', { 'username_icontains': 'INPUT_VALUE' })
    get_ajax_filter('Name', User, 'username', { 'FIELD_NAME_icontains': 'INPUT_VALUE' })
    
And these two leads also to same query (but you can't write it with non empty field_query and without FIELD_NAME pattern):

    get_ajax_filter('Name', User, 'fname,lname')
    get_ajax_filter('Name', User, 'fname,lname', { 'FIELD_NAME_icontains': 'INPUT_VALUE' })
    
