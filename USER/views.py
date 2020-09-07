from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import UserProfile, UserCart
from PRODUCT.models import Product
from django.contrib.auth import get_user_model
from django.db.models import F

User = get_user_model()


def user_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=UserProfile.objects.get(user=request.user))
        if form.is_valid():
            form.save()
            return redirect('homepage')
        else:
            return HttpResponse('err')
    else:
        form = ProfileForm(instance=UserProfile.objects.get(user=request.user))
        return render(request, 'user/profile.html', {'form': form})


def cart(request):
    if request.user.is_authenticated:
        cart_items = UserCart.objects.filter(user_id=request.user.id)
        cart_price = cart_items.values_list('cart_item__product_selling_price', 'quantity')
        amt = 0
        for i in cart_price:
            amt += i[0] * i[1]
        context = {
            'cart_items': cart_items,
            'cart_price': amt,
        }
        return render(request, 'user/cart.html', context)
    else:
        return render(request, 'user/cart.html')


def add_item_to_cart(request):
    if request.is_ajax():
        if request.user.is_authenticated:
            pk = request.GET.get('pk')
            item = UserCart.objects.filter(cart_item_id=pk, user_id=request.user.id)
            if not item.exists():
                obj = UserCart.objects.create(
                    user=request.user,
                    cart_item=Product.objects.get(pk=pk)
                )
                obj.save()
            else:
                item.update(quantity=F('quantity') + 1)
            return HttpResponse('ok', status=200)

        else:
            return HttpResponse('un-authenticated', status=401)


def change_quantity(request):
    if request.is_ajax():
        if request.user.is_authenticated:
            pk = request.GET.get('pk')
            action = request.GET.get('action')
            item = UserCart.objects.filter(cart_item_id=pk, user_id=request.user.id)
            q = item.values('quantity')[0]
            if action == 'increment':
                item.update(quantity=F('quantity') + 1)
                return JsonResponse({'status': 200}, safe=False, status=200)
            elif action == 'decrement':
                if q['quantity']:
                    item.update(quantity=F('quantity') - 1)
                    return JsonResponse({'status': 200}, safe=False, status=200)
                else:
                    return JsonResponse({'status': 200, 'message': 'no more decrement possible'}, safe=False, status=200)


def remove_cart_item(request):
    if request.is_ajax():
        if request.user.is_authenticated:
            pk = request.GET.get('pk')
            UserCart.objects.filter(cart_item_id=pk, user_id=request.user.id).delete()
            return JsonResponse({'status': 200}, safe=False, status=200)
