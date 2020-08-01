from django.contrib import admin
from .models import *


@admin.register(MasterCategory)
class MasterCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(MobileSpecification)
class MobileSpecsAdmin(admin.ModelAdmin):
    pass
