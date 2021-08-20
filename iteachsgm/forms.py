from accounts.models import CustomUserAccounts
from django import forms
from .models import upload

class uploadForm(forms.ModelForm):
    # creator = forms.ModelChoiceField
    class Meta:
        model = upload
        fields = ('Name', 'Image', 'Description')
        # exclude = ('likes', )