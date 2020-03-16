from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
import requests
import myfitnesspal
import datetime

def home(request):
    client = myfitnesspal.Client('blafving@gmail.com')
    now = datetime.datetime.now()
    todaysummary = client.get_date(now.year, now.month, now.day)
    rtdict = {'todaysummary': todaysummary }
    return render(request, 'polls\home.html', rtdict)
