import json
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from rest_framework.fields import JSONField
from .models import TodoList, UploadImageTest
from .forms import DocumentForm
from django.contrib.auth import login, authenticate
from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.response import Response
from .serializers import ImageSerializer, TodoSerializer
from todo import serializers
from rest_framework import generics
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


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
    serializer = TodoSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def todoUpdate(request, pk):
    task = TodoList.objects.get(id=pk)
    serializer = TodoSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        print("****---------------------#####")
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def create(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        print("****---------------------##### ADDDD")
        serializer.save()
    return Response(serializer.data)


def todoView(request):
    all_todo_items = TodoList.objects.all()
    return HttpResponseRedirect('/todolist')
    return render(request, 'todo.html', {'all': all_todo_items})


'''def addTodo(request):
    instanceTodoItem = TodoList()
    instanceTodoItem.content = request.POST['insert']
    instanceTodoItem.save()
    all_todo_items = TodoList.objects.all()
    return render(request, 'todo.html', {'all_items': all_todo_items})'''


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


'''def simple_upload(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'upload.html')'''


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


class ImageViewSet(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = ImageSerializer(data=request.data, instance=request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
