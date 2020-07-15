from django.contrib.auth.models import User
from django.db import models


class ShopOwnerDetails(models.Model):
    shop_owner_name = models.CharField(max_length=255)
    shop_owner_contact_no = models.CharField(max_length=11)
    shop_owner_email_address = models.EmailField()
    shop_owner_contact_address = models.TextField()
    shop_owner_PAN_no = models.CharField(max_length=10)

    def __str__(self):
        return self.shop_owner_name


class ShopFeedback(models.Model):
    feedback_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    feedback = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)


class ShopRegistration(models.Model):
    PRODUCTS = [
        ('Electronic', 'Electronic'),
        ('Book', 'Book'),
        ('Clothes', 'Clothes'),
        ('Grocery', 'Grocery'),
    ]

    shop_owner = models.OneToOneField(ShopOwnerDetails, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=255)
    shop_address = models.TextField()
    shop_description = models.TextField()
    shop_email_address = models.EmailField()
    shop_verified = models.BooleanField(default=False)
    shop_state = models.CharField(max_length=200)
    shop_city = models.CharField(max_length=200)
    shop_pincode = models.CharField(max_length=6)
    shop_type = models.CharField(max_length=255, choices=PRODUCTS)
    shop_feedback = models.OneToOneField(ShopFeedback, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.shop_name
