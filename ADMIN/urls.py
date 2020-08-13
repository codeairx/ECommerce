from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.admin_login, name='admin_homepage'),
]
