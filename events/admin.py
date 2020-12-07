from django.contrib import admin
from .models import Event,SoloSinging,GroupEventPA

# Register your models here.
admin.site.register(Event)
admin.site.register(SoloSinging)
admin.site.register(GroupEventPA)