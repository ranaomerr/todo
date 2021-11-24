from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import DocumentForm
from django.contrib.auth import login, authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ImageUploadSerializer, TodoSerializer
from rest_framework import viewsets
from .models import ImageUpload, TodoList


@api_view(['GET'])
def todoOverview(request):
    api_urls = {
        'List': '/todolist/',
        'Create': '/todo-create/',
        'Update': '/todo-update/<str:pk>',
        'Delete': '/todo-delete/<str:pk>',
    }
    return Response(api_urls)


@api_view(['GET'])
def todoList(request):
    tasks = TodoList.objects.all()
    # "many" tells here that there are many items to serializers
    serializer = TodoSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def todoUpdate(request, pk):
    task = TodoList.objects.get(id=pk)
    serializer = TodoSerializer(instance=task, data=request.data)  # instance?
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def create(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


def todoView(request):
    all_todo_items = TodoList.objects.all()
    return HttpResponseRedirect('/todolist')
    return render(request, 'todo.html', {'all': all_todo_items})


def deleteTodo(request, todo_id):
    item_to_delete = TodoList.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')


def updateTodo(request, todo_id):
    update_to = request.POST.get('change')
    item_to_update = TodoList.objects.filter(
        id=todo_id).update(content=update_to)
    return HttpResponseRedirect('/todo/')


def update(request):
    all_todo_items = TodoList.objects.all()
    return render(request, 'update.html', {'all_items': all_todo_items})


def add(request):
    all_todo_items = TodoList.objects.all()
    return render(request, 'add.html', {'all_items': all_todo_items})


def go_to_signin(request):
    return render(request, 'register.html')


def register_user(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/list/')
    else:
        form = DocumentForm()
    return render(request, 'register.html', {'form': form})


def view(request):
    return render(request, 'view.html', {})


def logout(request):
    return render(request, 'logout.html', {})


class ImageUploadViewSet(viewsets.ModelViewSet):
    queryset = ImageUpload.objects.all()
    serializer_class = ImageUploadSerializer
