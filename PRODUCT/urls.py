from django.urls import path
from . import views

urlpatterns = [
    path('add-product/', views.add_product, name='add_product'),
    path('product-list/', views.product_list, name='productlist'),
    path('update-product-info/<str:pk>/', views.update_product_info, name='product_info_update'),
]
