import urllib

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

    Model = get_model(model_str)

    filter_query = {"%s__icontains"%field: query}
    exclude_query = {"pk__in": exclude}
    if fromlist:
        filter_query.update({"pk__in": fromlist })
    data = Model.objects.filter(**filter_query).exclude(**exclude_query).distinct(field).values_list("pk", field)

    return HttpResponse(simplejson.dumps(list(data)))

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
