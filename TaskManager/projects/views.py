from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm


def main_page(request):
    context = {

    }

    return render(request, 'projects/main.html', context=context)


def projects_list(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }

    return render(request, 'projects/projects_list.html', context=context)


def project_view(request, project_slug):
    project = Project.objects.get(slug=project_slug)

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('app_projects:projects_list')
    else:
        form = ProjectForm(instance=project)

    context = {
        'project': project,
        'form': form
    }

    return render(request, 'projects/project.html', context=context)


def create_project(request):
    form = ProjectForm

    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_projects:projects_list')
        else:
            print(form.errors)

    context = {
        'form': form
    }

    return render(request, 'projects/project_form.html', context=context)


def project_delete(request, project_slug):
    project = Project.objects.get(slug=project_slug)

    if request.method == "POST":
        project.delete()

        return redirect('app_projects:projects_list')