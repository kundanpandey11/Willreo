from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import CustomUserAccounts
from .forms import UserCreationForm, UserChangeForm


class CustomUserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'username', 'school', 'is_staff', 'is_superuser')
    list_filter = ('is_superuser',)

    fieldsets = (
        ('None', {'fields' : ('email', 'is_staff', 'is_superuser', 'password')}),
        ('Personal Info', {'fields' : ('username', 'school')}),
        ('Groups', {'fields':('groups',)}),
        ('Permission', {'fields': ('user_permissions',)}),
    )
    add_fieldsets = (
        ('None', {'fields' : ('email', 'password1', 'password2', 'is_staff', 'is_superuser')}),
        ('Personal Info', {'fields' : ('username', 'school')}),
        ('Groups', {'fields':('groups',)}),
        ('Permission', {'fields': {'user_permissions',}}),
    )

    
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()




admin.site.register(CustomUserAccounts, CustomUserAdmin)