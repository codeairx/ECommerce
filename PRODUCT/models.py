from django.db import models
from SELLER.models import ShopRegistration


class MasterCategory(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    parent_category = models.ForeignKey(MasterCategory, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=200)

    def __str__(self):
        return self.subcategory_name


class Product(models.Model):
    product_shop = models.ForeignKey(ShopRegistration, on_delete=models.CASCADE)
    product_master_category = models.ForeignKey(MasterCategory, on_delete=models.CASCADE)
    product_sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    product_stoke = models.IntegerField()
    product_MPR = models.IntegerField()
    product_selling_price = models.IntegerField()
    seller = models.ManyToManyField(ShopRegistration, related_name='seller_product')

    def __str__(self):
        return str(self.id)


# mobile section
class MobileSpecification(models.Model):
    shop = models.OneToOneField(Product, on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=100)
    mobile_name = models.CharField(max_length=100)
    starting_selling_price = models.BigIntegerField()
    mobile_display_size = models.FloatField()
    mobile_battery_capacity = models.IntegerField()

    def __str__(self):
        return self.mobile_name


class Mobilevariant(models.Model):
    mobile = models.ForeignKey(MobileSpecification, on_delete=models.CASCADE)
    RAM = models.IntegerField()
    storage = models.IntegerField()
    price_by_variant = models.BigIntegerField()

    def __str__(self):
        return self.mobile.mobile_name
    # mobile section end
