from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from .models import Accessory
from django.template import loader
from django.core.exceptions import PermissionDenied
def view_accessory(request):
    accessories = Accessory.objects.all()
    template = loader.get_template('accessory/accessory.html')
    context = {
        'accessories':accessories,
    }
    return HttpResponse(template.render(context, request))

def view_special_accessory(request, accessory_id):
    try:
       accessory = Accessory.objects.get(pk = accessory_id)
       template = loader.get_template('accessory/detail.html')
       context = {
        'accessory':accessory,
    }
    except Accessory.DoesNotExist:
        raise Http404('accessory does not exist')
    return HttpResponse(template.render(context, request))
