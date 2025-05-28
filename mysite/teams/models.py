from django.db import models

# Create your models here.

class TeamMember(models.Model):
    name = models.CharField(max_length=100)  # For the member's name
    position = models.CharField(max_length=100)  # For their role/position
    photo = models.ImageField(upload_to='team_photos/')  # For the member's photo

    def __str__(self):
        return self.name  # Returns the name when displaying the object

