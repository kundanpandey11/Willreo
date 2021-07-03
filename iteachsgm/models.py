import datetime
from django.db import models
from django.utils import timezone

class upload(models.Model):
    Name = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='pics')
    Description = models.CharField(max_length=2500)

    def __str__(self):
        return self.Name