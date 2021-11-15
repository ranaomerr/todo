from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem


def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html', {'all_items': all_todo_items})


def add(request):
    new_item = TodoItem(content=request.POST.get('context', ""))
    new_item.save()
    # return render(request, 'todo.html', {'all_items': all_todo_items})
    return HttpResponseRedirect('/todo/')


def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')


def updateTodo(request, todo_id):
    item = TodoItem.objects.get(id=todo_id)
    item_to_update = TodoItem.objects.filter(
        id=todo_id).update(content='omer')
    # item_to_update.save()
    return HttpResponseRedirect('/todo/')


def update(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'update.html', {'all_items': all_todo_items})
