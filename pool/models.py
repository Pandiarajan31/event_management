from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Item(models.Model):
    ITEM_TYPE = (
        ('V','Villa'),
        ('P','Plot'),
        ('F','Flat'),
    )
    CITY = (
        ('KOCHI','kochi'),
        ('TRIVANDRUM','trivandrum'),
        ('KOTTAYAM','kottayam'),
        ('THRISSUR','thrissur'),
        ('KOZHIKODE','kozhikode'),

    )
    event_title = models.CharField(max_length=50,null=True,blank=True)
    event_description = models.CharField(max_length=90,null=True,blank=True)
    event_images = models.ImageField(upload_to='realapp/images',null=True,blank=True)
    name = models.CharField(max_length=15,null=True,blank=True)
    contact_phone_no = models.IntegerField(null=True,blank=True)
    book=models.IntegerField(default=1)
    country=models.CharField(max_length=15,null=True,blank=True)


    def __str__(self):
        return self.name
