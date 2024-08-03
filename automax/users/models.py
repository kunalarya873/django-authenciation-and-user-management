from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from localflavor.in_.models import INStateField
from .utils import user_directory_path
# Create your models here.

class Location(models.Model):
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128, blank=True)
    state = INStateField(default="UP")
    zip_code = models.CharField(max_length=6)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_directory_path,null=True)
    bio = models.CharField(max_length=140, blank=True)
    phone_number = models.CharField(max_length=12)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)

    
    def __str__(self):
        return self.user.username
    