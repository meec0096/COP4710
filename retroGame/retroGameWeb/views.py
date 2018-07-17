from django.shortcuts import render
from django.http import HttpResponse
from .models import Region
''' constitutes as index.html without the css and javascript ''' 
def index(request):
    # Qeury similar to SELECT * from Region where regionid = 1
    region = Region.objects.get(regionid = 1)
    return HttpResponse(region.name)
# Create your views here.
