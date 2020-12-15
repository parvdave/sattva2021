from django.urls import path,include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('',views.home,name='landing-page'),
    path('<str:dept>',views.islandview,name='island-view'),
]
