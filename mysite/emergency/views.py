from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Emergency

def emergency_view(request):
    if request.method == 'POST':
        # Get form data
        emergency_name = request.POST.get('emergency_name')
        emergency_number = request.POST.get('emergency_number')
        address = request.POST.get('address')

        # Debug: Check if the form data is being captured correctly
        print(f"Emergency Name: {emergency_name}")
        print(f"Emergency Number: {emergency_number}")
        print(f"Address: {address}")

        if not emergency_name or not emergency_number or not address:
            return render(request, 'emergency/emergency.html', {'error': 'All fields are required'})
        # Save data to the database
        emergency = Emergency.objects.create(
            emergency_name=emergency_name,
            emergency_number=emergency_number,
            address=address,
        )

        # Send an email notification
        send_mail(
            subject=f"Emergency Request From: {emergency_number}",
            message=f"Emergency Details:\nName: {emergency_name}\nContact: ({emergency_number})\n _____Address_____:\n{address}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_RECEIVER],  # Replace with recipient email
            fail_silently=False,
        )

        return render(request, 'emergency/emergency_success.html', {'loaction': address})

    return render(request, 'emergency/emergency.html')