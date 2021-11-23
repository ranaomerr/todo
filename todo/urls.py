from rest_framework import routers
from django.urls import path, include
from .import views
from .models import TodoList, UploadImageTest
from rest_framework.routers import DefaultRouter
from todo.views import logout, ImageViewSet
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'my-model/', TodoList, basename='MyModel')

urlpatterns = [
    path('', views.todoOverview, name='todoOverview'),
    path('todolist', views.todoList, name='todoList'),
    path('update/<str:pk>/', views.todoUpdate, name='update'),

    path('create/', views.create, name='create'),
    path("upload/", include(DefaultRouter().urls)),
    path("token/", obtain_auth_token, name="rest_auth_token"),
    path("avatar/", ImageViewSet.as_view(), name="rest_user_avatar_upload"),

]
