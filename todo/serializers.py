from rest_framework import serializers
from .models import TodoList, UploadImageTest


# The ModelSerializer class provides a shortcut that lets you automatically create a Serializer class with fields that correspond to the Model fields.
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ('id', 'title', 'completed')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadImageTest
        fields = ["avatar"]

    def save(self, *args, **kwargs):
        if self.instance.avatar:
            self.instance.avatar.delete()
        return super().save(*args, **kwargs)
