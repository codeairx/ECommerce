from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ShopRegistrationForm


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
        form = ShopRegistrationForm()
        return render(request, 'shop/shopregister.html', {'form': form})
