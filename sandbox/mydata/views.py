from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Nutrient, User
import myfitnesspal
import datetime

def home(request):
    client = myfitnesspal.Client('blafving@gmail.com')
    try: 
        new = Nutrient.objects.create(date=datetime.date.today(), user_rec=User.objects.get(firstname='Brandon'))
    finally:
        nutrients = Nutrient.objects.all().order_by('date').reverse()
        rtdict = {
            'nutrients': nutrients, 
            }
        return render(request, 'mydata\home.html', rtdict)
