from rest_framework import routers
from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r"imageupload", views.ImageUploadViewSet)

urlpatterns = [
    path('', views.todoOverview, name='todoOverview'),
    path('list/', views.todoList, name='todoList'),
    path('update/<str:pk>/', views.todoUpdate, name='update'),

    path('create/', views.create, name='create'),
    path("imageupload/", include(router.urls)),

]
