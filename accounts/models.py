from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from .usermanger import AccountManager




class CustomUserAccounts(AbstractBaseUser, PermissionsMixin): 
    email = models.EmailField(_('email'),  unique=True)
    username = models.CharField(max_length=40, unique=True)
    school = models.CharField(max_length=150)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True)


    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'school']

    

    def __str__(self):
        return self.email



    