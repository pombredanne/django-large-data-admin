from django.db.models import get_model as django_get_model
from django.http import HttpResponse
from django.utils import simplejson
from django.template.defaultfilters import slugify
from django.shortcuts import render_to_response
from django.conf import settings

import importlib

def get_model(model_str):
    model = model_str.split(".")
    class_name = model[-1]
    module_name = ".".join(model[:-1])
    module = importlib.import_module(module_name)
    return getattr(module, class_name)

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

def selected_json(request, app, model, pk, field):
    value = request.GET.get("q")

    Model = get_model(app, model)
    instance = Model.objects.get(pk=pk)
    KeyModel = getattr(instance, field).model

    objs = getattr(instance, field).all()

    return HttpResponse(simplejson.dumps(objs.count()))


def select_add_json(request, model, pk, field):
    value = request.GET.get("q", "")
    data = []

    import importlib
    model = model.split(".")
    class_name = model[-1]
    module_name = ".".join(model[:-1])

    module = importlib.import_module(module_name)
    Model = getattr(module, class_name)
    objs = Model.objects.all()
    for obj in objs:
        if slugify(value) in slugify(obj.__unicode__()):
            data.append((obj.pk, obj.__unicode__()))

    return HttpResponse(simplejson.dumps(data))

def many_to_namy_list_add_view(request, app, model, pk, field):
    value = request.GET.get("q", "")
    data = []

    Model = get_model(app, model)
    instance = Model.objects.get(pk=pk)
    KeyModel = getattr(instance, field).model

    objs = KeyModel.objects.all()
    selected = getattr(instance, field).all()
    for obj in objs:
        if slugify(value) in slugify(obj.__unicode__()) and not obj in selected:
            data.append((obj.pk, obj.__unicode__()))

    return render_to_response("large_data_admin/widget_list_add.html",
        {
            "data": data,
            "STATIC_URL": settings.STATIC_URL,
            "app": app,
            "model": model,
            "field": field,
        },)


def many_to_namy_list_rm_view(request, app, model, pk, field):
    value = request.GET.get("q", "")
    data = []

    Model = get_model(app, model)
    instance = Model.objects.get(pk=pk)
    KeyModel = getattr(instance, field).model

    for obj in getattr(instance, field).all():
        if slugify(value) in slugify(obj.__unicode__()):
            data.append((obj.pk, obj.__unicode__()))

    return render_to_response("large_data_admin/widget_list_rm.html",
        {
            "data": data,
            "STATIC_URL": settings.STATIC_URL,
            "app": app,
            "model": model,
            "field": field,
        },)