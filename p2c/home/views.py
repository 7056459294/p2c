from django.shortcuts import render #p2c-21-085
from .models import *#p2c-21-085
def index(request):#p2c-21-085
    events = Events.objects.all() #p2c-21-085
    return render(request,'event.html',{'events':events}) #p2c-21-085

# Create your views here.
