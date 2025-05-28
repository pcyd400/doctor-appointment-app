from django.shortcuts import render

# Create your views here.
from .models import TeamMember  # Import the TeamMember model

def about(request):
    team_members = TeamMember.objects.all()  # Fetch all team members from the database
    return render(request, 'aboutus.html', {'team_members': team_members})  # Pass to template
