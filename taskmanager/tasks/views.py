from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Task
from .forms import TaskForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request:HttpRequest) -> HttpResponse:
    tasks = Task.objects.filter(user=request.user)
    return render(request, "tasks/index.html",{
        "tasks": tasks
    })

def  create_task(request:HttpRequest) -> HttpResponse:
    if request.method == "POST":
        task_form = TaskForm(request.POST)
        
        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('home')
        
    else:
        task_form = TaskForm()
        
    return render(request, "tasks/create_task.html",{
        "form": task_form
    })

def task_detail(request:HttpRequest, id:int) -> HttpResponse:
    task = get_object_or_404(Task, pk=id)
    return render(request, "tasks/task_detail.html", {
        "task": task
    })

def edit_task(request:HttpRequest, id:int) -> HttpResponse:
    task = get_object_or_404(Task, pk=id)
    
    if request.method =="POST":
        task_form = TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect("home")
    else:
        task_form = TaskForm(instance=task)
    
    return render(request, "tasks/edit_task.html", {
        "form": task_form,
        "task": task,
    })

def complete_task(request:HttpRequest, id:int) -> HttpResponse:
    task = get_object_or_404(Task, pk=id)
    if request.method == "POST":
        task.is_completed = True
        task.save()
    
    
    return redirect("detail", id=id)
    

def delete_task(request:HttpRequest, id:int) -> HttpResponse:
    task = get_object_or_404(Task, pk=id)
    if request.method == "POST":
        task.delete()
    
    return redirect("home")


def landing_page(request:HttpRequest) -> HttpResponse:
    return render(request, "landing.html")


def sign_up(request:HttpRequest) -> HttpResponse:
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect("login")
    else:
        user_form = UserCreationForm()
    
    return render(request, "registration/signup.html", {
        "user_form": user_form
    })