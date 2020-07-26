from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .models import ShopOwnerRegistration
from .forms import ShopRegisterForm, ShopOwnerRegisterForm, ShopOwnerBankForm, SellerLoginForm


def seller_login(request):
    if request.method == 'POST':
        form = SellerLoginForm(request.POST)
        if form.is_valid():
            user = ShopOwnerRegistration.objects.get(email=form.cleaned_data['email'])
            if check_password(form.cleaned_data['password'], user.password):
                login(request, user)
                print('ok')
                return redirect('homepage')
            else:
                return HttpResponse('wrong password')

    else:
        form = SellerLoginForm()
        return render(request, 'accounts/sellerlogin.html', {'form': form})


@login_required
def shop_owner_registration(request):
    if request.method == 'POST':
        form = ShopOwnerRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            return redirect('shop_registration')
        else:
            return HttpResponse('custom error')
    else:
        form1 = ShopOwnerRegisterForm()
        return render(request, 'shop/user_register.html', {'form1': form1})


@login_required
def shop_registration(request):
    if request.method == 'POST':
        form = ShopRegisterForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = ShopRegisterForm()
        return render(request, 'shop/shopregister.html', {'form': form})
