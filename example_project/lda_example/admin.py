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
