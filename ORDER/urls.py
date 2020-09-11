from django.urls import path
from . import views

urlpatterns = [
    path('address-select/', views.order_address, name='order_address'),
]
