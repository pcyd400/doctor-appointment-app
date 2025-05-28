from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact

def contact_view(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save data to the database
        contact = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        # Send an email notification
        send_mail(
            subject=f"New Contact Form Submission: {subject}",
            message=f"Message from:\nName: {name} Email: ({email})\n _____Message_____:\n{message}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_RECEIVER],  # Replace with recipient email
            fail_silently=False,
        )

        return render(request, 'contact/contact_success.html', {'name': name})

    return render(request, 'contact/contact.html')
