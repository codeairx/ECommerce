from django.contrib.auth.models import User
from django.db import models


class ShopOwnerRegistration(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    contact_address = models.TextField()
    TIN_number = models.CharField(max_length=11)

    def __str__(self):
        return self.name


class ShopRegistration(models.Model):
    SHOP_TYPES = [
        ('Electronic', 'Electronic'),
        ('Book', 'Book Depot'),
        ('Clothes', 'Clothes'),
        ('Grocery', 'Grocery'),
    ]

    owner = models.OneToOneField(ShopOwnerRegistration, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=150)
    shop_type = models.CharField(max_length=100, choices=SHOP_TYPES)
    shop_email_address = models.EmailField(null=True, blank=True)
    shop_address = models.TextField()
    shop_phone_number = models.CharField(max_length=13)
    shop_description = models.TextField(null=True, blank=True)
    shop_pincode = models.CharField(max_length=6)
    shop_state = models.CharField(max_length=200)
    shop_city = models.CharField(max_length=200)
    shop_verified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.shop_name)


class ShopOwnerBankDetails(models.Model):
    shop_owner = models.OneToOneField(ShopOwnerRegistration, on_delete=models.CASCADE)
    bank = models.CharField(max_length=255)
    account_no = models.CharField(max_length=20)
    IFSC_code = models.CharField(max_length=11)
    PAN_number = models.CharField(max_length=11)


class ShopFeedback(models.Model):
    feedback_user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback_shop = models.ForeignKey(ShopRegistration, on_delete=models.CASCADE)
    rating = models.IntegerField()
    feedback = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
