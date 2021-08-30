from django import forms 
from .models import CreateOrganization

class CreateOrganizationForm(forms.ModelForm):
    
    class Meta:
        model = CreateOrganization
        fields = ('organization_name', 'organization_leader_name')