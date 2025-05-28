from django.conf import settings
from django.shortcuts import render, redirect
from .models import Appointment
from django.core.mail import send_mail

def book_appointment(request):
    if request.method == 'POST':
        # Get data from the form
        patient_name = request.POST['patient_name']
        contact_number = request.POST['contact_number']
        appointment_date = request.POST['appointment_date']
        appointment_time = request.POST['appointment_time']

        # Create and save the appointment, generating the slug
        appointment = Appointment.objects.create(
            patient_name=patient_name,
            contact_number=contact_number,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
        )

        # Send an email notification
        send_mail(
            subject=f"New appointment booked from: {patient_name}",
            message=f"____details_____\n Name:{patient_name} \n Contact 📞:{contact_number} \n Date📅:({appointment_date}) \n Time⌚: {appointment_time}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_RECEIVER],
            fail_silently=False,
        )

        # Redirect to the success page with the slug
        return redirect('appointment_successful', slug=appointment.slug)

    return render(request, 'appointment/appointment.html')


def appointment_successful(request, slug):
    # Fetch the appointment using the slug
    appointment = Appointment.objects.get(slug=slug)

    # Render the success page with appointment details
    return render(request, 'appointment/appointment_success.html', {'appointment': appointment})
