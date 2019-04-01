from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Project
from .forms import NewProjectForm

def projects_today(request):
    all_projects= Project.objectS.all()
    if form.is_valid():
        HttpResponseRedirect('projects_today')
    else:
        form = NewProjectForm()
    return render(request, 'all-projects/projects.html', {"ProjectForm":form, "projects":all_projects})

def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_project = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-projects/search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-projects/search.html',{"message":message})

    def new_project(request):
    
        current_user = request.user
        title = 'New project'
        if request.method == 'POST':
            form = NewProjectForm(request.POST, request.FILES)
            if form.is_valid():
                project = form.save(commit=False)
                project.user = current_user
                project.save()
            return redirect('projectsToday')

        else:
            form = NewProjectForm()
        return render(request, 'new_project.html', {"form": form,"current_user":current_user,"title":title})