from rest_framework import serializers
from .models import TodoList, ImageUpload


# The ModelSerializer class provides a shortcut that lets you automatically create a Serializer class with fields that correspond to the Model fields.
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ('id', 'title', 'completed')


class ImageUploadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ImageUpload
        fields = ('title', 'image')
