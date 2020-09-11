from django.shortcuts import render, redirect
from USER.models import UserProfile


def order_address(request):
    if request.user.is_authenticated:
        user = UserProfile.objects.get(user=request.user)
        address = [user.delivery_address1, user.delivery_address2]
        context = {
            'name': user.name,
            'mobile_no': user.phone_number,
            'address': address
        }
        return render(request, 'order/order_address.html', context)

    else:
        return redirect('loginpage')
