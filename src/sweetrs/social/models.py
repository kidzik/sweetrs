from django.db import models
from django.contrib.auth.models import User

__author__ = 'kidzik'

class Friendship(models.Model):
    user1 = models.ForeignKey(User, related_name="friends_hosted")
    user2 = models.ForeignKey(User, related_name="friends_guested")