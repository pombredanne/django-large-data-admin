import urllib

from django.http import HttpResponse
from django.utils import simplejson
from django.template.defaultfilters import slugify
from django.shortcuts import render_to_response, render
from django.conf import settings

from helpers import get_model, getattr2

def add_json(request, model_str):
    data = []

    q = request.GET.get("q", "")
    exclude = []
    for e in request.GET.get("s", "").split(","):
        try:
            exclude.append(int(e))
        except ValueError:
            pass

    Model = get_model(model_str)

    for obj in Model.objects.exclude(pk__in=exclude):
        if slugify(q) in slugify(obj.__unicode__()) and not obj.pk in exclude:
            data.append((obj.pk, obj.__unicode__()))

    return HttpResponse(simplejson.dumps(data))

def rm_json(request, model_str):
    data = []

    q = request.GET.get("q", "")
    selected = []
    for s in request.GET.get("s", "").split(","):
        try:
            selected.append(int(s))
        except ValueError:
            pass

    Model = get_model(model_str)

    for obj in Model.objects.filter(pk__in=selected):
        if slugify(q) in slugify(obj.__unicode__()):
            data.append((obj.pk, obj.__unicode__()))

    return HttpResponse(simplejson.dumps(data))

def check_json(request, model_str):
    data = []

    q = request.GET.get("q", "")
    selected = []
    for s in request.GET.get("s", "").split(","):
        try:
            selected.append(int(s))
        except ValueError:
            pass

    Model = get_model(model_str)

    for obj in Model.objects.filter(pk__in=selected):
        if slugify(q) in slugify(obj.__unicode__()):
            data.append((obj.pk, obj.__unicode__()))

    return HttpResponse(simplejson.dumps(data))

def get_json(request):
    model_str = request.GET.get("model")
    field = request.GET.get("field")
    query = urllib.unquote(request.GET.get("query", ""))
    exclude = filter(None, request.GET.get("exclude", "").split(","))

    Model = get_model(model_str)

    filter_query = {"%s__icontains"%field: query}
    exclude_query = {"pk__in": exclude}
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
