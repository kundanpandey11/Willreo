from django import forms
from .models import upload

class uploadForm(forms.ModelForm):
    class Meta:
        model = upload
        fields = ('Name', 'Image', 'Description')