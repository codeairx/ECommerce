from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.seller_home, name='seller_home'),
    path('user-register/', views.shop_owner_registration, name='shop_owner_registration'),
    path('seller-register/', views.shop_registration, name='shop_registration'),
    path('bank-account-details/', views.bank_account_register, name='bank_account_page'),
    path('profile/', views.seller_profile, name='seller_profile'),
]
