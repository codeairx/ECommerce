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


# MOBILE SECTION START
class MobileSpecification(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=100)
    mobile_name = models.CharField(max_length=100)
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


# MOBILE SECTION END

# LAPTOP SECTION START
class Laptop(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    brand = models.CharField(max_length=200)
    model_name = models.TextField()
    description = models.TextField()


class LaptopVariant(models.Model):
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    processor = models.CharField(max_length=255)
    RAM = models.IntegerField()
    storage = models.CharField(max_length=100)
    price_by_variant = models.BigIntegerField()


# LAPTOP SECTION END


# BOOK SECTION START
class Book(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=200)
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.book_title


class Novel(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    novel_title = models.CharField(max_length=255)
    novel_author = models.CharField(max_length=255)

    def __str__(self):
        return self.novel_title

# BOOK SECTION END
