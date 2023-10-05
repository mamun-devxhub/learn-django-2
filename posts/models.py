"""imports"""
from django.db import models


class Post(models.Model):
    """Post model"""
    text = models.TextField()

    def __str__(self):
        """string representation"""
        return self.text[:50]
