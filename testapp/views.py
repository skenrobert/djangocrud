#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project,Task #import models
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject

# from django.contrib.auth.models import User
# from django.db import IntegrityError

from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    title = 'Django home'
    return render(request, 'index.html', {
        'title': title
    })

def about(request):
    return HttpResponse("About")

def hello(request, username): #http://127.0.0.1:8000/hello/kenny
    print(username)#console
    return HttpResponse("<h1>Hello %s</h1>" % username)#print variable 

def showprojects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)
    
def showtasks(request, id):
    task = Task.objects.get(id=id)
    task = get_object_or_404(Task, id=id)
    return HttpResponse("task %s" % task.title)
    
def tasks(request):
    # tasks = Task.objects.all()
    # tasks = Task.objects.filter(user=request.user)#that only belong to that user
    # tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True) #that are also null in the completed field
    tasks = Task.objects.filter(datecompleted__isnull=True) #that are also null in the completed field
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })
    
def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })
    
def create_task(request):
    print(request)
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        try:
            # Task.objects.create(
            #     title=request.POST['title'], description=request.POST['description'], project_id=1)
            #all task is belong project id 1, recomendation create select with all project for the user to select
            form = CreateNewTask(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user #user login save in request
            new_task.project_id = 1
            new_task.save()
            print(new_task)
            
            return redirect('tasks')
        except ValueError:
         return render(request, 'tasks/create_task.html', {"form": CreateNewTask, "error": "Error creating task."})

    
def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST["name"])
        return redirect('projects')

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })
    
@login_required
def task_detail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = CreateNewTask(instance=task)
        return render(request, 'tasks/task_detail.html', {'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = CreateNewTask(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'tasks/task_detail.html', {'task': task, 'form': form, 'error': 'Error updating task.'})
        
@login_required
def tasks_completed(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'tasks/tasks.html', {"tasks": tasks})

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
    
@login_required
def signout(request):
    logout(request)
    return redirect('home')