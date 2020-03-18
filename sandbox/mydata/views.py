from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Nutrient
import requests
import myfitnesspal
import datetime

def home(request):
    client = myfitnesspal.Client('blafving@gmail.com')
    todaysummary = client.get_date(datetime.datetime.today())
    nutrients = Nutrient.objects.all()
    rtdict = {
        'todaysummary': todaysummary, 
        'nutrients': nutrients 
        }
    return render(request, 'mydata\home.html', rtdict)
