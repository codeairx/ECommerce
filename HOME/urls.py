from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('view-product-info/<str:pk>/', views.product_detail, name='product_detail_page'),
]
