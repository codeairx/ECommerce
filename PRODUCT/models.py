from django.db import models
from SELLER.models import ShopRegistration


class Prouduct(models.Model):
    shop = models.ForeignKey(ShopRegistration, on_delete=models.CASCADE)


class ProductCategory(models.Model):
    category = models.ForeignKey(Prouduct, on_delete=models.CASCADE)
