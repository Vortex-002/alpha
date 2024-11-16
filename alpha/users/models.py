from django.db import models
from django.contrib.auth.models import AbstractUser 

class CustomUser (AbstractUser ):

    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='/home/s/code/root/alpha/alpha/profile_pictures', blank=True, null=True)

    def __str__(self):
        return self.username