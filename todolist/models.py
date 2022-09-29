from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    usernames = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    date = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title