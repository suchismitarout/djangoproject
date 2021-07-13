from django.db import models


# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=8)
    location = models.CharField(max_length=30)
