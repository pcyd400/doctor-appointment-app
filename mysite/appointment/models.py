from django.db import models
from django.utils.text import slugify

class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    booking_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)  # Add a slug field

    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate a slug based on the patient's name and appointment date
            self.slug = slugify(f"{self.patient_name}-{self.appointment_date}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.patient_name} - {self.appointment_date} at {self.appointment_time}"
