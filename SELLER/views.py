from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .models import ShopOwnerRegistration
from .forms import ShopRegisterForm, ShopOwnerRegisterForm, ShopOwnerBankForm


def shop_owner_registration(request):
    if request.method == 'POST':
        form = ShopOwnerRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            # error
            login(request, request.user)
            return redirect('shop_registration')
        else:
            return HttpResponse('custom error')
    else:
        form1 = ShopOwnerRegisterForm()
        return render(request, 'shop/user_register.html', {'form1': form1})


def shop_registration(request):
    if request.method == 'POST':
        form = ShopRegisterForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = ShopRegisterForm(instance=ShopOwnerRegistration.objects.get(id=request.user.id))
        return render(request, 'shop/shopregister.html', {'form': form})
