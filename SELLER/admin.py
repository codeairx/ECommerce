from django.contrib import admin
from .models import *


@admin.register(ShopRegistration)
class RegisterShopAdmin(admin.ModelAdmin):
    pass


@admin.register(ShopFeedback)
class ShopFeedbackAdmin(admin.ModelAdmin):
    pass


@admin.register(ShopOwnerProfile)
class ShopOwnerAdmin(admin.ModelAdmin):
    pass


@admin.register(ShopOwnerBankDetails)
class ShopOwnerAdmin(admin.ModelAdmin):
    pass
