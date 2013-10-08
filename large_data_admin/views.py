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

def fk_add_json(request, model_str):
    value = request.GET.get("q", "") 
    data = []

    Model = get_model(model_str)
    
    for obj in Model.objects.all():
        if slugify(value) in slugify(obj.__unicode__()):
            data.append((obj.pk, obj.__unicode__()))

    return HttpResponse(simplejson.dumps(data))

def filter_json(request, model_str, field):
    data = []
    field = field.replace("__", ".")

    q = request.GET.get("q", "")
    Model = get_model(model_str)

    f = {"%s__icontains"%field:q}
    data = list(Model.objects.filter(**f).values_list("pk", field, field))
    data_keys = []
    data2 = []
    for i in range(len(data)):
        if data[i][1] not in data_keys:
            data2.append(data[i])
        data_keys.append(data[i][1])

    return HttpResponse(simplejson.dumps(data2))


def filter_attribute_json(request, model_str, field):
    data = []
    field = field.replace("__", ".")

    q = request.GET.get("q", "")
    exclude = []

    Model = get_model(model_str)

    f = {"%s__icontains"%field:q}
    data = list(Model.objects.filter(**f).values_list("pk", field, field))
    data_keys = []
    data2 = []
    for i in range(len(data)):
        if data[i][1] not in data_keys:
            data2.append(data[i])
        data_keys.append(data[i][1])

    return HttpResponse(simplejson.dumps(data2))

def m2m_list_view(request, model_str):
    try:
        pks = [int(pk) for pk in request.GET.get("q", "").split(",")]
    except ValueError:
        pks = ()
    Model = get_model(model_str)
    objs = Model.objects.filter(pk__in=pks)

    return render(request, "large_data_admin/m2m/list.html", {
        "objs": objs,
    })

def m2m_remove_view(request, model_str):
    pks = [int(pk) for pk in request.GET.get("q", "").split(",")]
    Model = get_model(model_str)
    objs = Model.objects.filter(pk__in=pks)

    return render(request, "large_data_admin/m2m/remove.html", {
        "objs": objs,
    })
