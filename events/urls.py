from django.contrib import admin
from django.urls import path,include
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('<str:event>/', views.Renderform.as_view(),name="form-view"),
]