from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class ShopOwnerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10, unique=True)
    contact_address = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tbl_shop_owner_profile'


class ShopRegistration(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=150)
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

    class Meta:
        db_table = 'tbl_registered_shops'


class ShopOwnerBankDetails(models.Model):
    shop_owner = models.OneToOneField(User, on_delete=models.CASCADE)
    bank = models.CharField(max_length=255)
    account_no = models.CharField(max_length=20)
    IFSC_code = models.CharField(max_length=11)
    PAN_number = models.CharField(max_length=11)

    def __str__(self):
        return self.shop_owner.name

    class Meta:
        db_table = 'tbl_shop_owner_bank_details'


class ShopFeedback(models.Model):
    feedback_user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback_shop = models.ForeignKey(ShopRegistration, on_delete=models.CASCADE)
    rating = models.IntegerField()
    feedback = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
