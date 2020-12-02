from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.image,name="image-test"),
]
