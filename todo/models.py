from django.db import models
import datetime
from django.utils import timezone


class TodoItem(models.Model):
    content = models.TextField()
    description = models.CharField(max_length=200)
    # uploaded_at = models.DateField(
    #    blank=True, null=True, default=datetime.date.today)
    # uploaded_at = models.DateTimeField(
    #   default=timezone.now)
    #uploaded_at = models.DateTimeField(auto_now_add=True)
    document = models.FileField(upload_to='documents/', default="")
    uploaded_at = models.DateTimeField(auto_now_add=True)
