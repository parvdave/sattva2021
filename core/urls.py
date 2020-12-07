from django.contrib import admin
from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('', views.image,name="image-test"),
    path('<str:dept>/',views.jsonitems,name="core-info")
]
