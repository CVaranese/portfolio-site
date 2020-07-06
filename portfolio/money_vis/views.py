import requests

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    ctxt = {}
    
    return render(request, 'money_vis/index.html', ctxt)
