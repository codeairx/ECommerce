from django.db import models


class UserProfile(models.Model):
    phone_number = models.CharField(max_length=10)
    delivery_address1 = models.TextField()
    delivery_address2 = models.TextField()
