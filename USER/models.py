from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=10)
    delivery_address1 = models.TextField(blank=True, null=True)
    delivery_address2 = models.TextField(blank=True, null=True)
