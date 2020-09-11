from django.db import models
from PRODUCT.models import Product


class Order(models.Model):
    ADDRESS_TYPE = [
        ('Home', 'Home'),
        ('Office', 'Office'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=10)
    alternate_mobile_no = models.CharField(max_length=10, null=True, blank=True)
    pincode = models.CharField(max_length=6)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    landmark = models.CharField(max_length=255)
    address_type = models.CharField(max_length=10, choices=ADDRESS_TYPE)
    order_datetime = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=255)

    class Meta:
        db_table = 'tbl_user_orders'
