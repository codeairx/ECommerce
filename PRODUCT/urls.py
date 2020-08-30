from django.urls import path
from . import views

urlpatterns = [
    path('add-product/', views.add_product, name='add_product'),
    path('product-list/', views.product_list, name='productlist'),
    path('update-product-info/<str:pk>/', views.update_product_info, name='product_info_update'),
    path('product/info/<str:pk>/', views.product_stock_update, name='product_stoke_update'),
    path('product-live/', views.set_product_live, name='live-product'),
    path('category-filter/', views.filter_product_type, name='category filter'),
]
