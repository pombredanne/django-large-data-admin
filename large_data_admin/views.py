from django.http import HttpResponse
from django.utils import simplejson
from django.template.defaultfilters import slugify
from django.shortcuts import render_to_response
from django.conf import settings

from helpers import get_model

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
