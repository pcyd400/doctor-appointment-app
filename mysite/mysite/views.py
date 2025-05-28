from django.http import HttpResponse

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')  # Render the index.html for the home page

def contact(request):
    return render(request, 'contact.html')  # Render the contact.html for the contact page

def appointment(request):
    return render(request, 'appointment.html')  # Render the appointment.html for the appointment page
def about(request):
    return render(request, 'aboutus.html')  # Render the aboutus.html for the anout page
def emergency(request):
    return render(request, 'emergency/emergency.html')  # Render the emergency.html for the emergency page
