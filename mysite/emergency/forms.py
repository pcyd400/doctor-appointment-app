
from django import forms
from .models import Emergency

class EmergencyForm(forms.ModelForm):
    class Meta:
        model = Emergency
        fields = ['emergency_name', 'emergency_number', 'address']
