from django.contrib import admin
from .models import Event,SoloSinging,GroupSinging
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Event)
@admin.register(SoloSinging)
@admin.register(GroupSinging)

class ViewAdmin(ImportExportModelAdmin):
    pass