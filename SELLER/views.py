from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ShopRegistrationForm, ShopOwnerDetailsForm, ShopOwnerProfileForm


@login_required
def shop_registration(request):
    if request.method == 'POST':
        form = ShopRegistrationForm(request.POST)
        if form.is_valid():
            owner = form.save(commit=False)
            owner.shop_owner = User.objects.get(id=request.user.id)
            owner.save()
            return HttpResponse('ok')
    else:
        form3 = ShopRegistrationForm()
        form1 = ShopOwnerDetailsForm(instance=request.user)
        form2 = ShopOwnerProfileForm()

        args = {
            'form1': form1,
            'form2': form2,
            'form3': form3
        }

        return render(request, 'shop/shopregister.html', args)
