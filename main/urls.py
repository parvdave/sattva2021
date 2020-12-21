from django.urls import path,include
from . import views
from django.views.generic import TemplateView

app_name='main'

urlpatterns = [
    path('',views.home,name='landing-page'),
    path('depts/<str:dept>',views.islandview,name='island-view'),
]
