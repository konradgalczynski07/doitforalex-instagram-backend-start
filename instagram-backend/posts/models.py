import uuid
from django.db import models
from django.conf import settings


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_posts'
    )
    photo = models.ImageField(blank=False, editable=False)
    text = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="likers", blank=True, symmetrical=False
    )

    class Meta:
        ordering = ['-posted_on']

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return f'{self.author}\'s post'
