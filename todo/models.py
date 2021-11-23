from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import os


class TodoList(models.Model):
    # user = models.ForeignKey(
    #    User, on_delete=models.CASCADE, related_name="todolist", null=True)

    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.title


def upload_to(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 1000
    return f"users/{instance.pk}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"
    return '/'.join(['images', str(instance.name), filename])


class UploadImageTest(AbstractUser):
    #name = models.CharField(max_length=200)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
