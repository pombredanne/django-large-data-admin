from django.db.models import get_model
from django.http import HttpResponse
from django.utils import simplejson
from django.template.defaultfilters import slugify

def add_json(request, app, model, pk, field):
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

    return HttpResponse(simplejson.dumps(data))

def rm_json(request, app, model, pk, field):
    value = request.GET.get("q", "")
    data = []

    Model = get_model(app, model)
    instance = Model.objects.get(pk=pk)
    KeyModel = getattr(instance, field).model

    for obj in getattr(instance, field).all():
        if slugify(value) in slugify(obj.__unicode__()):
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
    value = request.GET.get("q", "")
    data = []

    Model = get_model(app, model)
    instance = Model.objects.get(pk=pk)
    KeyModel = getattr(instance, field).model

    objs = getattr(instance, field).all()
    for obj in objs:
        if slugify(value) in slugify(obj.__unicode__()):
            data.append((obj.pk, obj.__unicode__()))

    return HttpResponse(simplejson.dumps(data))

def selected_json(request, app, model, pk, field):
    value = request.GET.get("q")

    Model = get_model(app, model)
    instance = Model.objects.get(pk=pk)
    KeyModel = getattr(instance, field).model

    objs = getattr(instance, field).all()

    return HttpResponse(simplejson.dumps(objs.count()))


def select_add_json(request, model):
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

    return HttpResponse(simplejson.dumps(data))


def many_to_namy_list_rm_view(request, app, model, pk, field):
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

    return HttpResponse(simplejson.dumps(data))