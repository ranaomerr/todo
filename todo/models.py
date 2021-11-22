from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class TodoList(models.Model):
    # user = models.ForeignKey(
    #    User, on_delete=models.CASCADE, related_name="todolist", null=True)

    name = models.CharField(max_length=200)
    content = models.TextField()
    description = models.CharField(max_length=200)
    document = models.FileField(upload_to='documents/', default="")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class TodoItem(models.Model):
    # todolist = models.OneToOneField(
    #   TodoList, on_delete=models.CASCADE, primary_key=True)
    # todolist = models.ForeignKey(
    #    TodoList, on_delete=models.CASCADE, default="")
    content = models.TextField()
    description = models.CharField(max_length=200)
    document = models.FileField(upload_to='documents/', default="")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.description
