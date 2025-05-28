from django.urls import path
from .views import emergency_view

urlpatterns = [
    path('', emergency_view, name='emergency'),
]