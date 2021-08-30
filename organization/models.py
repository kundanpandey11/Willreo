from django.db import models
from django.conf import settings
from django.db.models.deletion import PROTECT
from django.db.models.fields import BLANK_CHOICE_DASH

class CreateOrganization(models.Model):
    organization_name = models.CharField(max_length=200, blank=False, unique=True)
    organization_leader_name = models.CharField(max_length=200, blank=False)
    organization_creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    organization_create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.organization_name

    
