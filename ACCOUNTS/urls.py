from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='loginpage'),
    path('signup/', views.signup_user, name='signuppage'),
    path('logout/', views.logout_user, name='logout')
]
