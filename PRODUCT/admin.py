from django.contrib import admin
from .models import Category, ProductType


@admin.register(Category)
class Category(admin.ModelAdmin):
    pass


@admin.register(ProductType)
class Category(admin.ModelAdmin):
    pass
