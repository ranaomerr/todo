from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem


def todoView(request):
    all_todo_items = TodoItem.objects.all()

    return render(request, 'todo.html', {'all_items': all_todo_items})


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
