import requests

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    api_key = 'Ksj9W0U9cIEmxqtCbpSXa77Yy4TATCFCnJPYB261'
    ctxt = {}
    
    return render(request, 'money_vis/index.html', ctxt)
