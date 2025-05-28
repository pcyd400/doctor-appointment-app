from django.db import models

class Emergency(models.Model):
    emergency_name = models.CharField(max_length=255)
    emergency_number = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set to current timestamp when created

    def __str__(self):
        return self.emergency_name
