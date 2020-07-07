from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    ctxt = {}
    return render(request, 'portfolio/index.html', ctxt)

def projects(request):
    ctxt = {}
    return render(request, 'portfolio/projects.html', ctxt)
