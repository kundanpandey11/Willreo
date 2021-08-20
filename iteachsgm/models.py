from accounts.models import CustomUserAccounts
from django.db import models
from django.utils import timezone
from django.conf import settings


class upload(models.Model):
    Name = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='pics')
    Description = models.CharField(max_length=2500)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="likes")


    def __str__(self):
        return self.Name 

    @property
    def total_likes(self):
        return self.likes.all().count()