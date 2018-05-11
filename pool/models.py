from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager)
from django.contrib.auth.models import PermissionsMixin
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation



# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self,email,password=None, mobile_no=None,name=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            mobile_no=mobile_no,
            name=name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password,name,mobile_no):
        user=self.create_user(
        email,
        password=password,name=name,mobile_no=mobile_no
    )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser=True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, unique=True, null=True)
    mobile_no = models.IntegerField(null = True)

    is_staff = models.BooleanField(('staff status'), default=False,)
    is_superuser = models.BooleanField(('staff status'),default=False)

    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'mobile_no']



class Item(models.Model):
    event_title = models.CharField(max_length=50)
    event_description = models.TextField()
    event_images = models.ImageField(upload_to='event/images')
    detailed_images = models.ImageField(upload_to='event/images')
    name = models.CharField(max_length=15)
    contact_phone_no = models.IntegerField()
    price=models.IntegerField(default=1)
    venue=models.CharField(max_length=15)
    date=models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(UserProfile,on_delete = models.CASCADE,)
    item = models.ForeignKey(Item,on_delete = models.CASCADE,null=True,blank=True)
    comment = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.user.email

