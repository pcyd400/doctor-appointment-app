from django.contrib import admin

# Register your models here.
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'contact_number', 'appointment_date', 'appointment_time', 'booking_date')
    list_filter = ('appointment_date',)
    search_fields = ('patient_name', 'contact_number')

