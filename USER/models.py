from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=10)
    delivery_address1 = models.TextField()
    delivery_address2 = models.TextField()
