from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.shop_registration, name='shop_registration'),
]
