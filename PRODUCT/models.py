from django.db import models
from SELLER.models import ShopRegistration


class Product(models.Model):
    shop = models.OneToOneField(ShopRegistration, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_description = models.TextField()
    product_MRP = models.IntegerField()
    product_price = models.BigIntegerField()
    product_discount = models.IntegerField()
