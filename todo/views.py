from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import TodoItem
from .forms import DocumentForm

from django.contrib.auth import login, authenticate
from django.contrib import messages


def todoView(request):
    all_todo_items = TodoItem.objects.all()

    return render(request, 'todo.html', {'all': all_todo_items})


def addTodo(request):
    instanceTodoItem = TodoItem()
    instanceTodoItem.content = request.POST['insert']
    instanceTodoItem.save()
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html', {'all_items': all_todo_items})


def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')


def updateTodo(request, todo_id):
    update_to = request.POST.get('change')
    item_to_update = TodoItem.objects.filter(
        id=todo_id).update(content=update_to)
    return HttpResponseRedirect('/todo/')


def update(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'update.html', {'all_items': all_todo_items})


def add(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'add.html', {'all_items': all_todo_items})


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('todo')
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {
        'form': form
    })


def go_to_signin(request):
    return render(request, 'register.html')


def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/todo/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
