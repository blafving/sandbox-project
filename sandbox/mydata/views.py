from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Nutrient
from .utils import log_myfitpal
import myfitnesspal
import datetime

def home(request):
    client = myfitnesspal.Client('blafving@gmail.com')
    log_myfitpal('blafving@gmail.com', datetime.date.today())
    nutrients = Nutrient.objects.all().order_by('date').reverse()
    rtdict = {
        'nutrients': nutrients 
        }
    return render(request, 'mydata\home.html', rtdict)
