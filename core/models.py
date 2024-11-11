from django.contrib.auth.models import User  # Import the User model
from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=200)
    participants = models.ManyToManyField(User, related_name="events_participated", blank=True)

    def __str__(self):
        return self.title
