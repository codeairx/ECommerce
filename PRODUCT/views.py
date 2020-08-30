from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core import serializers
from .models import *
from .forms import *


def filter_product_type(request):
    if request.is_ajax():
        pk = request.GET.get('pk')
        serializerData = serializers.serialize('json', ProductType.objects.filter(category_id=pk))
        return JsonResponse(serializerData, safe=False)


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

        obj = Product.objects.create(
            product_shop_id=request.user.shopregistration.id,
            product_category=request.POST.get('product_category'),
            product_type=request.POST.get('product_type'),
            brand=request.POST.get('product_brand'),
            product_home_img=request.FILES['product_image'],
            product_name=request.POST.get('product_name'),
            product_stoke=request.POST.get('product_stoke'),
            product_MRP=request.POST.get('product_MPR'),
            product_selling_price=request.POST.get('product_selling_price')
        )
        obj.save()
        return redirect('productlist')
    else:
        context = {
            'category': Category.objects.all()
        }
        return render(request, 'product/addproduct.html', context)


@login_required
@user_passes_test(lambda u: u.is_seller, login_url='/seller/user-register/')
def product_list(request):
    products = Product.objects.filter(product_shop_id=request.user.shopregistration.id).order_by('-id')
    context = {'products': products}
    return render(request, 'product/product_list.html', context)


@login_required
@user_passes_test(lambda u: u.is_seller, login_url='/seller/user-register/')
def product_stock_update(request, pk):
    product = Product.objects.get(pk=pk)
    shop = ShopRegistration.objects.get(owner_id=request.user.id)
    print(shop.id)

    if request.method == 'POST':
        postForm = StokeUpdateForm(request.POST, instance=product)
        if postForm.is_valid():
            form = postForm.save(commit=False)
            form.product_shop_id = shop.id
            form.save()
            return redirect('productlist')
    else:
        try:
            getForm = StokeUpdateForm(instance=product)
        except Product.DoesNotExist:
            getForm = StokeUpdateForm()

        context = {
            'pk': pk,
            'product': product,
            'form': getForm
        }
        return render(request, 'product/update_stock_details.html', context)


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
                                                   instance=MobileDetails.objects.get(product_id=pk))
            except MobileDetails.DoesNotExist:
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
                postForm = LaptopSpecificationForm(request.POST, instance=LaptopDetails.objects.get(product_id=pk))
            except LaptopDetails.DoesNotExist:
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
                postForm = EarphoneForm(request.POST, instance=Earphones.objects.get(product_id=pk))
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
                getForm = MobileSpecificationForm(instance=MobileDetails.objects.get(product_id=pk))
            except MobileDetails.DoesNotExist:
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
                getForm = LaptopSpecificationForm(instance=LaptopDetails.objects.get(product_id=pk))
            except LaptopDetails.DoesNotExist:
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
