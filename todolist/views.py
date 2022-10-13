from django.shortcuts import render
from todolist.models import Task

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound

from django.urls import reverse
from django.core import serializers

from todolist.forms import TaskForm

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_task = Task.objects.all().filter(usernames=request.user)
    context = {
        'list_task': data_task,
        'usernames': request.user.get_username(),
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def task_user(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            task = Task()
            task.usernames = request.user
            task.date = datetime.datetime.now()
            task.title = form.cleaned_data['title']
            task.description = form.cleaned_data['description']
            task.save()
            messages.success(request, 'Task telah berhasil dibuat!')
            return HttpResponseRedirect(reverse('todolist:show_todolist'))

    return render(request, 'createtask.html', {'form': form})

def task_delete(request, id):
    data_task = Task.objects.get(id=id)
    data_task.delete()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))


@login_required(login_url='/todolist/login/')
def todolist_json(request):
    data_task = Task.objects.all().filter(usernames=request.user)
    return HttpResponse(serializers.serialize('json', data_task), content_type="application/json")

@login_required(login_url='/todolist/login/')
def todolist_add(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")

        task = Task.objects.create(title=title, description=description, date=datetime.date.today(), usernames=request.user)
        task.save()
        result = {
            'fields':{
                'title': task.title,
                'description': task.description,
                'date': task.date,
            },
            'pk': task.pk
        }

        return HttpResponse(b"CREATED", status=200)

    return HttpResponseNotFound()