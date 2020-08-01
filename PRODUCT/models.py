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
    product_name = models.CharField(max_length=255)
    product_stoke = models.IntegerField()
    product_MRP = models.IntegerField()
    product_selling_price = models.IntegerField()
    seller = models.ManyToManyField(ShopRegistration, related_name='seller_product_table')

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
    # ome_page_photo = models.ImageField(upload_to='phone_home_photos/')
    # Brand Details
    brand = models.CharField(max_length=200)
    phone_name = models.CharField(max_length=200)
    model_name = models.CharField(max_length=200, null=True)
    launch_date = models.DateField(null=True)

    # Body dimension
    # dimensions = models.CharField(max_length=200, null=True)
    # weight = models.FloatField(null=True)
    # build = models.CharField(choices=BUILD_TYPES, max_length=100)
    # # display
    # display_type = models.CharField(choices=DISPLAY_TYPES, max_length=100)
    # display_size = models.CharField(max_length=200)
    # display_refresh_rate = models.CharField(choices=REFRESH_RATE, max_length=100)
    # display_resolution = models.CharField(max_length=200)
    # display_protection = models.CharField(choices=PROTECTION_TYPE, max_length=150)
    # HDR_support = models.BooleanField(default=True)
    # # Platform
    # UI_name = models.CharField(max_length=200)
    # android_version = models.CharField(choices=ANDROID_VERSION, max_length=150)
    # ios_version = models.CharField(max_length=100, choices=IOS_VERSION)
    # processor = models.CharField(max_length=200)
    # gpu = models.CharField(max_length=200, null=True)
    # # Network
    # network_technology = models.CharField(max_length=200, null=True)
    # SIM_Type = models.CharField(choices=SIM_TYPE, max_length=150)
    # wifi_technology = models.CharField(max_length=200, null=True)
    # bluetooth = models.CharField(choices=BLUETOOTH_TECH, max_length=100)
    # GPS = models.CharField(max_length=200, null=True)
    # radio = models.BooleanField(default=True)
    # NFC = models.BooleanField(default=False)
    # # Memory
    # RAM_Type = models.CharField(choices=RAM_TYPES, max_length=50)
    # expandable_storage = models.BooleanField()
    # storage_type = models.CharField(choices=STORAGE_TYPE, max_length=100)
    # RAM = models.IntegerField()
    # internal_storage = models.IntegerField()
    # # Back Camera
    # back_camera_setup = models.CharField(max_length=190)
    # back_camera_resolution = models.TextField(blank=True)
    # back_camera_features = models.TextField(blank=True)
    # back_camera_video_features = models.TextField(blank=True)
    # back_camera_flash = models.BooleanField()
    # # Front Camera
    # front_camera_setup = models.CharField(max_length=190)
    # front_camera_resolution = models.TextField(blank=True)
    # front_camera_features = models.TextField(blank=True)
    # front_camera_flash = models.BooleanField()
    # front_camera_video_features = models.TextField(blank=True)
    # # Sound
    # loudspeaker = models.CharField(max_length=100, choices=SPEAKER)
    # audio_jack = models.CharField(max_length=100, choices=AUDIO_JACK)
    # audio_features = models.CharField(max_length=200, blank=True)
    # # Battery
    # battery_capacity = models.CharField(max_length=200)
    # battery_type = models.CharField(choices=BATTERY_TYPE, max_length=100)
    # fast_charging = models.BooleanField(default=True)
    # charging_output = models.CharField(max_length=200, blank=True)
    # charging_port = models.CharField(max_length=100, choices=CHARGING_PORT)
    # reverse_charging = models.BooleanField(default=True)
    # wireless_charging = models.BooleanField()
    # # Others
    # fingerprint_sensor = models.CharField(choices=FINGERPRINT, max_length=200)
    # face_unlock = models.BooleanField(default=True)
    # other_sensors = models.TextField(blank=True)
    # description = models.TextField(blank=True)
    # rating = models.FloatField(blank=True)

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
