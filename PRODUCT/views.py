from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *


def set_product_live(request):
    if request.is_ajax():
        pk = request.POST.get('pk')
        checked = request.POST.get('checked')
        if checked == 'true':
            item = Product.objects.get(pk=pk)
            item.is_product_live = True
            item.save()
            return JsonResponse({'success': True}, status=200)
        else:
            item = Product.objects.get(pk=pk)
            item.is_product_live = False
            item.save()
            return JsonResponse({'success': True}, status=200)


@login_required
@user_passes_test(lambda u: u.is_seller, login_url='/seller/user-register/')
def add_product(request):
    if request.method == 'POST':

        category = request.POST.get('product_category')
        product_type = request.POST.get('product_type')
        stoke = request.POST.get('product_stoke')
        name = request.POST.get('product_name')
        MRP = request.POST.get('product_MPR')
        price = request.POST.get('product_selling_price')

        obj = Product.objects.create(
            product_shop_id=request.user.shopregistration.id,
            product_category_id=category,
            product_type=product_type,
            product_name=name,
            product_stoke=stoke,
            product_MRP=MRP,
            product_selling_price=price
        )
        obj.save()
        return redirect('productlist')
    else:
        category = Category.objects.all()
        args = {
            'category': category
        }
        return render(request, 'product/addproduct.html', args)


@login_required
@user_passes_test(lambda u: u.is_seller, login_url='/seller/user-register/')
def product_list(request):
    products = Product.objects.filter(product_shop_id=request.user.shopregistration.id).order_by('-id')
    context = {'products': products}
    return render(request, 'product/product_list.html', context)


@login_required
@user_passes_test(lambda u: u.is_seller, login_url='/seller/user-register/')
def update_product_info(request, pk):
    product = Product.objects.get(pk=pk)
    # POST METHODS
    if request.method == 'POST':
        # MOBILE
        if product.product_category.category_name == 'Mobile':
            try:
                postForm = MobileSpecificationForm(request.POST,
                                                   instance=MobileSpecification.objects.get(product_id=pk))
            except MobileSpecification.DoesNotExist:
                postForm = MobileSpecificationForm(request.POST)

            if postForm.is_valid():
                obj = postForm.save(commit=False)
                obj.product = product
                obj.save()
                return redirect('productlist')
            else:
                return HttpResponse('err')

        # LAPTOP
        elif product.product_category.category_name == 'Laptop':
            try:
                postForm = LaptopSpecificationForm(request.POST, instance=Laptop.objects.get(product_id=pk))
            except Laptop.DoesNotExist:
                postForm = LaptopSpecificationForm(request.POST)

            if postForm.is_valid():
                obj = postForm.save(commit=False)
                obj.product = product
                obj.save()
                return redirect('productlist')
            else:
                return HttpResponse('err')

        # EARPHONES
        elif product.product_type == 'earphone':
            try:
                postForm = EarphoneForm(request.POST, instance=Laptop.objects.get(product_id=pk))
            except Earphones.DoesNotExist:
                postForm = EarphoneForm(request.POST)

            if postForm.is_valid():
                obj = postForm.save(commit=False)
                obj.product = product
                obj.save()
                return redirect('productlist')
            else:
                return HttpResponse('err')

        # PHONE CHARGER
        elif product.product_type == 'phone charger':
            try:
                postForm = PhoneChargerForm(request.POST, instance=PhoneCharger.objects.get(product_id=pk))
            except PhoneCharger.DoesNotExist:
                postForm = PhoneChargerForm(request.POST)

            if postForm.is_valid():
                obj = postForm.save(commit=False)
                obj.product = product
                obj.save()
                return redirect('productlist')
            else:
                return HttpResponse('err')



    # GET METHODS
    else:
        # MOBILE
        if product.product_category.category_name == 'Mobile':
            try:
                getForm = MobileSpecificationForm(instance=MobileSpecification.objects.get(product_id=pk))
            except MobileSpecification.DoesNotExist:
                getForm = MobileSpecificationForm()

            product_name = Product.objects.get(pk=pk)

            context = {
                'form': getForm,
                'id': pk,
                'product_name': product_name.product_name
            }
            return render(request, 'product/product_info_update.html', context)


        # LAPTOP
        elif product.product_category.category_name == 'Laptop':
            try:
                getForm = LaptopSpecificationForm(instance=Laptop.objects.get(product_id=pk))
            except Laptop.DoesNotExist:
                getForm = LaptopSpecificationForm()

            product_name = Product.objects.get(pk=pk)

            context = {
                'form': getForm,
                'id': pk,
                'product_name': product_name
            }
            return render(request, 'product/product_info_update.html', context)


        # EARPHONE
        elif product.product_type == 'earphone':
            try:
                getForm = EarphoneForm(instance=Earphones.objects.get(product_id=pk))
            except Earphones.DoesNotExist:
                getForm = EarphoneForm()

            product_name = Product.objects.get(pk=pk)

            context = {
                'form': getForm,
                'id': pk,
                'product_name': product_name
            }
            return render(request, 'product/product_info_update.html', context)


        # PHONE CHARGER
        elif product.product_type == 'phone charger':
            try:
                getForm = PhoneChargerForm(instance=PhoneCharger.objects.get(product_id=pk))
            except PhoneCharger.DoesNotExist:
                getForm = PhoneChargerForm()

            product_name = Product.objects.get(pk=pk)

            context = {
                'form': getForm,
                'id': pk,
                'product_name': product_name
            }
            return render(request, 'product/product_info_update.html', context)
