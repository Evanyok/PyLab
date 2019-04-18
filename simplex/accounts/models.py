from django.db import models
from django.utils import timezone

class TUser(models.Model):
    username  = models.CharField(max_length=64, unique=True)
    password  = models.CharField(max_length=128)
    nickname  = models.CharField(max_length=64, unique=True)
    email     = models.CharField(max_length=32, unique=True)
    validated = models.BooleanField(default=False) 
    deleted   = models.BooleanField(default=False)
    created   = models.DateTimeField()

