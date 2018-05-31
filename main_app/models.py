"""Models."""

from django.db import models
from django.contrib.auth.models import User


class Share(models.Model):
    """Share model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.TextField()
    share_date = models.DateTimeField()

    def __str__(self):
        """Default text output."""
        return self.story
