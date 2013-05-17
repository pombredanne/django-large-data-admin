from django.db.models import get_model
from django.http import HttpResponse
from django.utils import simplejson

def add_json(request, app, model, pk, field):
    value = request.GET.get("q")
    data = []

    Model = get_model(app, model)
    instance = Model.objects.get(pk=pk)
    KeyModel = getattr(instance, field).model

    objs = KeyModel.objects.all()
    selected = getattr(instance, field).all()
    print objs
    print selected

    for obj in objs:
        if value in obj.__unicode__() and not obj in selected:
            data.append((obj.pk, obj.__unicode__()))

    print data
    return HttpResponse(simplejson.dumps(data))

def rm_json(request, app, model, pk, field):
    value = request.GET.get("q")
    data = []

    Model = get_model(app, model)
    instance = Model.objects.get(pk=pk)
    KeyModel = getattr(instance, field).model

    for obj in getattr(instance, field).all():
        if value in obj.__unicode__():
            data.append((obj.pk, obj.__unicode__()))

    return HttpResponse(simplejson.dumps(data))

def add_process(request, app, model, pk, field, value):
    Model = get_model(app, model)
    instance = Model.objects.get(pk=pk)
    KeyModel = getattr(instance, field).model

    getattr(instance, field).add(value)
    return HttpResponse("")

def rm_process(request, app, model, pk, field, value):
    Model = get_model(app, model)
    instance = Model.objects.get(pk=pk)
    KeyModel = getattr(instance, field).model

    getattr(instance, field).remove(value)
    return HttpResponse("")

def check_json(request, app, model, pk, field):
    value = request.GET.get("q")
    data = []

    Model = get_model(app, model)
    instance = Model.objects.get(pk=pk)
    KeyModel = getattr(instance, field).model

    objs = getattr(instance, field).all()
    print objs
    for obj in objs:
        if value in obj.__unicode__():
            data.append((obj.pk, obj.__unicode__()))

    return HttpResponse(simplejson.dumps(data))

def selected_json(request, app, model, pk, field):
    value = request.GET.get("q")

    Model = get_model(app, model)
    instance = Model.objects.get(pk=pk)
    KeyModel = getattr(instance, field).model

    objs = getattr(instance, field).all()

    return HttpResponse(simplejson.dumps(objs.count()))
