from django.contrib import admin
from .models import Item,Comment
from django.contrib.auth.models import User
from .models import *

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Item)
admin.site.register(Comment)
