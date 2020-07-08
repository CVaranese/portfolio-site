from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles import finders
import os
import yaml
from pathlib import Path
import mistune

# Create your views here.
def index(request):
    ctxt = {'projects': [
        {'image': 'images/image5.png',
         'name': 'Prediction of Steering Angles',
         'description': 'Using Keras to predict steering angles from images of the road',
         'link': 'https://google.com'},
        {'image': 'images/melee_thumb.jpg',
         'name': 'Super Smash Bros. Melee AI',
         'description': 'Creation of a Machine Learning Melee AI Using Keras',
         'link': 'https://google.com'},
        {'image': 'images/OW_thumb.jpg',
         'name': 'Overwatch Fight Prediction',
         'description': 'Final part of a Data Science project to predict the winners of fights in Overwatch',
         'link': 'https://google.com'},
        {'image': 'images/vlight_thumb.png',
         'name': 'Volumetric Lighting',
         'description': 'OpenGL implementation of Volumetric Lighting',
         'link': 'https://google.com'},
    ]}
    project_files_dir = finders.find('portfolio/projects/')
    project_files = os.listdir(project_files_dir)
    print(project_files)
    ctxt = {'projects': []}
    '''
    for project in project_files:
        with open(Path(project_files_dir).joinpath(project)) as pfile:
            file_details = yaml.load(pfile, Loader=yaml.FullLoader)
            file_details['link'] = project.split('.')[0]
            print(file_details)
            ctxt['projects'].append(file_details)
    '''

    return render(request, 'portfolio/index.html', ctxt)

def project_page(request, project_name):
    project_file = finders.find(f'portfolio/projects/{project_name}.md')
    print(project_file)
    with open(project_file) as pfile:
        file_content = pfile.read()
        #project_details = yaml.load(pfile, Loader=yaml.FullLoader)

    ctxt = {
        'name': project_name,
        'content': mistune.html(file_content),
    }

    #ctxt = project_details
    print(ctxt)
    return render(request, 'portfolio/project.html', ctxt)

def resume(request):
    return render(request, 'portfolio/resume.html')
