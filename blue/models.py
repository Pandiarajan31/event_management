from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    Name = models.CharField(max_length=20)
    Venue = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now())

class Viewers(models.Model):
    Customer_name=models.CharField(max_length=20)
    mailid=models.CharField(max_length=20)
    place=models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now())


