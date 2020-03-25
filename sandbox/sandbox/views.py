from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
import requests

def home(request):
    return render(request, 'sandbox\dashboard.html')
