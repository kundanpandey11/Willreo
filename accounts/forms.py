from django import forms
from django.forms.widgets import PasswordInput
from .models import CustomUserAccounts
from django.contrib.auth.forms import ReadOnlyPasswordHashField




class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = CustomUserAccounts
        fields = ('email', 'username', 'school', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='password1', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password2', widget=forms.PasswordInput)

    class Meta:
        model = CustomUserAccounts
        fields = ('email', 'username', 'school', 'password1', 'password2',)

        def cleaned_password2(self):
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 and password2 and password1 != password2:
                raise ValueError('Your passwords do not match')
            return password2


        def save(self, commit=True):
            user = super().save(commit=False)
            user.set_password(self.cleaned_data['password2'])
            if commit:
                user.save()
            return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUserAccounts
        fields = ('email', 'username','school', 'password', 'is_active', 'is_superuser')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]