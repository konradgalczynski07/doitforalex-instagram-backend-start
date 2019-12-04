from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    fullname = models.CharField(max_length=60, blank=True)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(default='avatar.png')
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="user_followers",
        blank=True,
        symmetrical=False,
    )
    following = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="user_following",
        blank=True,
        symmetrical=False,
    )

    def number_of_followers(self):
        return self.followers.count()

    def number_of_following(self):
        return self.following.count()

    def __str__(self):
        return self.username
