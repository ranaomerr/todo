from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import os
from django.contrib.auth.models import AbstractBaseUser


class TodoList(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.title


class ImageUpload(models.Model):
    title = models.CharField(max_length=50)
    images = models.ImageField('images')
