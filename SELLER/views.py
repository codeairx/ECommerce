from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import ShopOwnerProfile
from .forms import ShopRegisterForm, ShopOwnerProfileForm, ShopOwnerBankForm, SellerLoginForm


@login_required
@staff_member_required(login_url='/seller/user-register/')
def seller_home(request):
    return render(request, 'shop/sellerhome.html')


@login_required
def shop_owner_registration(request):
    if request.method == 'POST':
        form = ShopOwnerProfileForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            user_obj = User.objects.get(id=request.user.id)
            user_obj.is_staff = True
            user_obj.save()
            user.save()
            return redirect('shop_registration')
        else:
            return HttpResponse('custom error')
    else:
        form1 = ShopOwnerProfileForm(instance=User.objects.get(id=request.user.id))
        return render(request, 'shop/user_register.html', {'form1': form1})


@login_required
def shop_registration(request):
    if request.method == 'POST':
        form = ShopRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.owner = request.user
            user.save()
            return redirect('bank_account_page')
    else:
        form = ShopRegisterForm()
        return render(request, 'shop/shopregister.html', {'form': form})


@login_required
def bank_account_register(request):
    if request.method == 'POST':
        form = ShopOwnerBankForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.shop_owner = request.user
            user.save()
            return redirect('seller_home')
        else:
            return HttpResponse('error')
    else:
        form = ShopOwnerBankForm()
        return render(request, 'shop/bankdetailadd.html', {'form': form})
