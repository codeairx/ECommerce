from django.contrib.auth.models import User
from django.db import models


class ShopOwnerDetails(models.Model):
    shop_owner_name = models.CharField(max_length=255)
    shop_owner_contact_no = models.CharField(max_length=11)
    shop_owner_email_address = models.EmailField()
    shop_owner_contact_address = models.TextField()
    shop_owner_PAN_no = models.CharField(max_length=10)


class ShopFeedback(models.Model):
    feedback_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    feedback = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)


class ShopRegistration(models.Model):
    shop_owner = models.OneToOneField(ShopOwnerDetails, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=255)
    shop_address = models.TextField()
    shop_description = models.TextField()
    shop_email_address = models.EmailField()
    shop_verified = models.BooleanField(default=False)
    shop_feedback = models.OneToOneField(ShopFeedback, on_delete=models.CASCADE)


class Product(models.Model):
    PRODUCTS = [
        ('Electronic', 'Electronic'),
        ('Book', 'Book'),
        ('Clothes', 'Clothes'),
        ('Grocery', 'Grocery'),
    ]
    shop = models.OneToOneField(ShopRegistration, on_delete=models.CASCADE)
    product_category = models.CharField(choices=PRODUCTS, max_length=100)
    product_price = models.BigIntegerField()
