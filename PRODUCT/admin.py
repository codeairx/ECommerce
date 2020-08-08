from django.contrib import admin
from .models import *


@admin.register(Category)
class SubCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(MobileSpecification)
class MobileSpecsAdmin(admin.ModelAdmin):
    pass
