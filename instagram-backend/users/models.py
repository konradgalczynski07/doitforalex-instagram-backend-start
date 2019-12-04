from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    fullname = models.CharField(max_length=60, blank=True)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(default='avatar.png')

    def __str__(self):
        return self.username
