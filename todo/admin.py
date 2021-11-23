from django.contrib import admin

from django.contrib.auth.models import User

from .models import UploadImageTest
from .models import TodoList
admin.site.register(TodoList)
admin.site.register(UploadImageTest)
