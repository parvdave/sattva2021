from django.contrib import admin
from .models import Event,SoloSinging,GroupEventPA
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Event)
@admin.register(SoloSinging)
@admin.register(GroupEventPA)

class ViewAdmin(ImportExportModelAdmin):
    pass