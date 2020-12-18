from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from .models import Member
import json
app_name = "core"

# Create your views here.
def image(request):
    return render(request,'core/image.html',{})

def jsonitems(request,dept):
    coreinfo = serializers.serialize("json",Member.objects.all().filter(deptName__icontains=dept).order_by('posnum','firstName'))
    coreinfo = json.loads(coreinfo)
    return JsonResponse(coreinfo,safe=False)