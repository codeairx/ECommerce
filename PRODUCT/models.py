from django.db import models
from SELLER.models import ShopRegistration


class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_shop = models.ForeignKey(ShopRegistration, on_delete=models.CASCADE)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_type = models.CharField(max_length=100)
    product_name = models.CharField(max_length=255)
    product_stoke = models.IntegerField()
    product_MRP = models.IntegerField()
    product_selling_price = models.IntegerField()

    def __str__(self):
        return str(self.product_name)


# MOBILE SECTION START
class MobileSpecification(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    RAM_TYPES = [
        ('LPDDR3', 'LPDDR3'),
        ('LPDDR4', 'LPDDR4'),
        ('LPDDR4x', 'LPDDR4x'),
        ('LPDDR5', 'LPDDR5'),
    ]

    BUILD_TYPES = [
        ('Plastic Back', 'Plastic Back'),
        ('Glass Back', 'Glass Back'),
        ('Leather', 'Leather'),
        ('Other', 'Other'),
    ]

    DISPLAY_TYPES = [
        ('LCD', 'LCD'),
        ('IPS', 'IPS'),
        ('AMOLED', 'AMOLED'),
        ('S-AMOLED', 'S-AMOLED'),
        ('OLED', 'OLED'),
        ('RATINA', 'RATINA'),
    ]

    REFRESH_RATE = [
        ('60', '60 HZ'),
        ('90', '90 HZ'),
        ('120', '120 HZ'),
        ('144', '144 HZ'),
    ]

    PROTECTION_TYPE = [
        ('Gorila Glass 3', 'Gorila Glass 3'),
        ('Gorila Glass 4', 'Gorila Glass 4'),
        ('Gorila Glass 5', 'Gorila Glass 5'),
        ('Gorila Glass 6', 'Gorila Glass 6'),
    ]

    ANDROID_VERSION = [
        ('No', 'No'),
        ('Android 8.0', 'Android 8.0'),
        ('Android 9.0', 'Android 9.0'),
        ('Android 10.0', 'Android 10.0'),
        ('Android 11.0', 'Android 11.0'),
    ]

    IOS_VERSION = [
        ('10', '10'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('No IOS', 'No IOS'),
    ]

    SIM_TYPE = [
        ('Single Sim', 'Single Sim'),
        ('Dual Sim', 'Dual Sim'),
        ('Dual Sim with e-sim', 'Dual Sim with e-sim'),
        ('e-sim', 'e-sim'),
    ]

    BLUETOOTH_TECH = [
        ('4', 'Bluetooth 4'),
        ('4.1', 'Bluetooth 4.1'),
        ('4.2', 'Bluetooth 4.2'),
        ('5', 'Bluetooth 5'),
        ('5.1', 'Bluetooth 5.1'),
        ('5.2', 'Bluetooth 5.2'),
    ]

    STORAGE_TYPE = [
        ('eMMC 5.1', 'eMMC 5.1'),
        ('UFS 2.0', 'UFS 2.0'),
        ('UFS 2.1', 'UFS 2.1'),
        ('UFS 3.0', 'UFS 3.0'),
        ('UFS 3.1', 'UFS 3.1'),
    ]

    BATTERY_TYPE = [
        ('Li-ion', 'Li-ion'),
        ('Li-poly', 'Li-poly'),
    ]

    FINGERPRINT = [
        ('IN-Display', 'IN-Display'),
        ('Side Mounted', 'Side Mounted'),
        ('Rear Mounted', 'Rear Mounted'),
        ('No Fingerprint Sensor', 'No Fingerprint Sensor'),
    ]

    PHONE_TYPE = [
        ('Android', 'Android'),
        ('iPhone', 'iPhone'),
        ('Feature Phone', 'Feature Phone'),
        ('Tablet', 'Tablet')
    ]

    SPEAKER = [
        ('Single Speaker', 'Single Speaker'),
        ('Dual Speaker', 'Dual Speaker'),
    ]

    AUDIO_JACK = [
        ('3.5 mm Audio Jack', '3.5 mm Audio Jack'),
        ('Type C output', 'Type C Output'),
        ('No Jack Available', 'No Jack Available'),
    ]

    CHARGING_PORT = [
        ('Type C', 'Type C'),
        ('Micro USB', 'Micro USB'),
        ('Lighting', 'Lighting'),
    ]

    phone_type = models.CharField(max_length=100, choices=PHONE_TYPE)
    brand = models.CharField(max_length=200)
    phone_name = models.CharField(max_length=200)

    def __str__(self):
        return self.phone_name


# MOBILE SECTION END


# LAPTOP SECTION START
class Laptop(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    brand = models.CharField(max_length=200)
    model_name = models.TextField()
    description = models.TextField()
    processor = models.CharField(max_length=255)
    RAM = models.IntegerField()
    storage = models.CharField(max_length=100)
    price = models.BigIntegerField()

    def __str__(self):
        return self.model_name


# LAPTOP SECTION END

class PhoneCharger(models.Model):
    CHARGER_TYPES = [
        ('Type C', 'Type C'),
        ('Micro USB', 'Micro USB'),
        ('Lighting', 'Lighting'),
    ]

    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    charger_output = models.CharField(max_length=3)
    charger_type = models.CharField(max_length=50, choices=CHARGER_TYPES)


class LaptopCharger(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    charger_output = models.CharField(max_length=3)


class Earphones(models.Model):
    EARPHONE_TYPES = [
        ('Wired', 'Wired'),
        ('Bluetooth', 'Bluetooth'),
        ('Truly Wireless', 'Truly Wireless'),
    ]

    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=20)
    earphone_type = models.CharField(max_length=50, choices=EARPHONE_TYPES)
