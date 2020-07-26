from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.seller_login, name='seller_login'),
    path('user-register/', views.shop_owner_registration, name='shop_owner_registration'),
    path('shop-register/', views.shop_registration, name='shop_registration'),
]
