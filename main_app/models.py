"""Models."""

from django.db import models
#from django.contrib.auth.models import User


class User(models.Model):
    """User model."""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    motto = models.CharField(max_length=1000)

    def __str__(self):
        """Default text output."""
        return self.username


class Share(models.Model):
    """Share model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.TextField()
    post_date = models.DateTimeField()
    media = models.TextField()
    share_date = models.DateTimeField()

    def __str__(self):
        """Default text output."""
        return self.story
