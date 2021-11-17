from django import forms
from .models import TodoItem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class DocumentForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = TodoItem
        fields = ('content', 'description', 'document', )
