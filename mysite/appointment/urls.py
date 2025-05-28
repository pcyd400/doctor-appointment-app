from django.urls import path
from .views import book_appointment, appointment_successful

urlpatterns = [
    path('', book_appointment, name='appointment'),
    path('success/<slug:slug>/', appointment_successful, name='appointment_successful'),
]
