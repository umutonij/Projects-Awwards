from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Image

def projects(request):
    all_projects= Project.object.all
    if form.is_valid():
        HttpResponseRedirect('projects')
    else:
        form = NewProjectForm()
    return render(request, 'all-projects/projects.html', {"ProjectForm":form, "projects":all_projects})