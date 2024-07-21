from django.shortcuts import render
from .models import *
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')
def get_names(request):
    payload = []
    if search := request.GET.get('search'):
        objs= Names.objects.filter(name__startswith = search)
        payload.extend({'name': obj.name} for obj in objs)
    return JsonResponse({
        'status': True,
        'payload' : payload
    })
