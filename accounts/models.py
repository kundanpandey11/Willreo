from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models.deletion import CASCADE
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify, unordered_list
from django.urls import reverse
from .usermanger import AccountManager
import uuid



class CustomUserAccounts(AbstractBaseUser, PermissionsMixin): 
    email = models.EmailField(_('email'),  unique=True)
    username = models.CharField(max_length=40, unique=True)
    school = models.CharField(max_length=150)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True)
    slug = models.SlugField(unique=True, default=uuid.uuid1)


    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'school']

    class Meta:
        verbose_name_plural = 'Custom Users'

    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={'pk': self.pk})

    # 

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        return super().save(*args, **kwargs)

    def __str__(self):
        return (self.email)




