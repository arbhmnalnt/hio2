from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

class FinalRecordAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'created_at')

admin.site.register(FinalRecord, FinalRecordAdmin)
