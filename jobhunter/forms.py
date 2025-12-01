from django import forms 
from .models import JobApplication

class JobForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['company', 'position', 'status', 'date_applied']