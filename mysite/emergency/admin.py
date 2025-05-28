from django.contrib import admin
from .models import Emergency

@admin.register(Emergency)
class EmergencyAdmin(admin.ModelAdmin):
    list_display = ('emergency_name',  'address','created_at')
    search_fields = ('emergency_name', 'emergency_number', 'address')
    ordering = ('created_at',)

