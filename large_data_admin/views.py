import urllib, json

from django.http import HttpResponse
from django.utils import simplejson
from django.template.defaultfilters import slugify
from django.shortcuts import render_to_response, render
from django.conf import settings

from helpers import get_model

def get_json(request):
    model_str = request.GET.get("model")
    field = request.GET.get("field")
    query = urllib.unquote(request.GET.get("query", ""))
    exclude = filter(None, request.GET.get("exclude", "").split(","))
    fromlist = filter(None, request.GET.get("fromlist", "").split(","))
    unique = request.GET.get("unique")
    try:
        filter_query  = json.loads(urllib.unquote(request.GET.get("filter_query")))
    except:
        filter_query = {}
    try:
        exclude_query = json.loads(urllib.unquote(request.GET.get("exclude_query")))
    except:
        exclude_query = {}

    Model = get_model(model_str)

    if (len(filter_query) + len(exclude_query)) == 0:
        filter_query = {"%s__icontains"%field: query}
        exclude_query = {"pk__in": exclude}

    if fromlist:
        filter_query.update({"pk__in": fromlist })

    qs = Model.objects.filter(**filter_query).exclude(**exclude_query)

    if unique:
        try:  # XXX: needs prety check if DISTINCT is available, ticket #3
            return HttpResponse(simplejson.dumps(list(qs.distinct(field).values_list("pk", field))))
        except NotImplementedError:
            data = []
            unique_by_field = []
            for pk, field_value in list(qs.values_list("pk", field)):
                if field_value not in unique_by_field:
                    data.append((pk, field_value))
                unique_by_field.append(field_value)
            return HttpResponse(simplejson.dumps(data))

    return HttpResponse(simplejson.dumps(list(qs.values_list("pk", field))))

def m2m_list_view(request, model_str):
    pks = [int(pk) for pk in filter(None, request.GET.get("q", "").split(","))]
    Model = get_model(model_str)
    objs = Model.objects.filter(pk__in=pks)

    return render(request, "large_data_admin/m2m/list.html", {
        "objs": objs,
    })

def m2m_remove_view(request, model_str):
    pks = [int(pk) for pk in filter(None, request.GET.get("q", "").split(","))]
    Model = get_model(model_str)
    objs = Model.objects.filter(pk__in=pks)

    return render(request, "large_data_admin/m2m/remove.html", {
        "objs": objs,
    })
