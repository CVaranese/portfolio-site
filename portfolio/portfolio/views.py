from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    ctxt = {'projects': [
        {'image': 'images/melee_thumb.jpg',
         'name': 'Super Smash Bros. Melee AI',
         'subheading': 'What goes here',
         'description': 'Creation of a Machine Learning Melee AI Using Keras',
         'link': 'https://google.com'},
        {'image': 'images/OW_thumb.jpg',
         'name': 'Overwatch Fight Prediction',
         'subheading': 'What goes here',
         'description': 'Final part of a Data Science project to predict the winners of fights in Overwatch',
         'link': 'https://google.com'},
        {'image': 'images/vlight_thumb.png',
         'name': 'Volumetric Lighting',
         'subheading': 'What goes here',
         'description': 'OpenGL implementation of Volumetric Lighting',
         'link': 'https://google.com'},
        {'image': 'images/image5.png',
         'name': 'Prediction of Steering Angles',
         'subheading': 'What goes here',
         'description': 'Using Keras to predict steering angles from images of the road',
         'link': 'https://google.com'},
    ]}
    return render(request, 'portfolio/index.html', ctxt)

def resume(request):
    return render(request, 'portfolio/resume.html')
