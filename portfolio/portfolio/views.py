from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles import finders
from django.template import Template, Context
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
    ctxt = {'projects': []}
    for project in project_files:
        project_path = Path(project_files_dir).joinpath(project)
        details, content = process_project_page(project_path)
        details['link'] = project.split('.')[0]
        ctxt['projects'].append(details)

    return render(request, 'portfolio/index.html', ctxt)

def process_project_page(project_page_path):
    with open(project_page_path) as pfile:
        project_details = ''
        for line in pfile:
            if line == '---\n':
                break
            project_details += line
        project_details = yaml.load(project_details, Loader=yaml.FullLoader)
        project_content = pfile.read()
    return project_details, project_content

def project_page(request, project_name):
    project_file = finders.find(f'portfolio/projects/{project_name}.md')
    details, content = process_project_page(project_file)
    content = Template(content).render(Context({}))
    content = mistune.html(content)
        #project_details = yaml.load(pfile, Loader=yaml.FullLoader)

    ctxt = {
        'name': project_name,
        'content': content,
    }
    ctxt.update(details)

    #ctxt = project_details
    return render(request, 'portfolio/project.html', ctxt)

def resume(request):
    return render(request, 'portfolio/resume.html')
