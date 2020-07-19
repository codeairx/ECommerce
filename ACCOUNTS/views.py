from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from .forms import UserCreateForm, UserLoginForm


def login_user(request):
    form = UserLoginForm()
    if request.method == 'POST':
        userform = UserLoginForm(request.POST)
        if userform.is_valid():
            user = authenticate(
                request,
                username=userform.cleaned_data['email'],
                password=userform.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                return redirect('loginpage')
    else:
        return render(request, 'accounts/loginpage.html', {"form": form})


def signup_user(request):
    form = UserCreateForm()
    if request.method == 'POST':
        userform = UserCreateForm(request.POST)
        if userform.is_valid():
            user = User.objects.create_user(
                username=userform.cleaned_data['email'],
                first_name=userform.cleaned_data['firstname'],
                last_name=userform.cleaned_data['lastname'],
                email=userform.cleaned_data['email'],
                password=userform.cleaned_data['password2']
            )
            user.save()
            login(request, user)
            return redirect('homepage')
        else:
            return redirect('signuppage')
    else:
        return render(request, 'accounts/signuppage.html', {"form": form})


def logout_user(request):
    logout(request)
    return redirect('homepage')
