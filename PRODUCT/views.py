from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *


@login_required
@user_passes_test(lambda u: u.is_seller, login_url='/seller/user-register/')
def add_product(request):
    if request.method == 'POST':
        psc = request.POST.get('product_sub_category')
        pmc = request.POST.get('product_master_category')
        stoke = request.POST.get('product_stoke')
        name = request.POST.get('product_name')
        MRP = request.POST.get('product_MPR')
        price = request.POST.get('product_selling_price')
        obj = Product.objects.create(
            product_shop_id=request.user.shopregistration.id,
            product_master_category_id=pmc,
            product_sub_category_id=psc,
            product_name=name,
            product_stoke=stoke,
            product_MRP=MRP,
            product_selling_price=price
        )
        obj.save()
        return redirect('productlist')
    else:
        mc = MasterCategory.objects.all()
        args = {
            'mc': mc
        }
        return render(request, 'product/addproduct.html', args)


def sub_cat_filter(request):
    pk = request.GET.get('pk')
    cat = SubCategory.objects.filter(parent_category_id=pk).values()
    return JsonResponse({'subcat': list(cat)}, safe=False)


@login_required
@user_passes_test(lambda u: u.is_seller, login_url='/seller/user-register/')
def product_list(request):
    products = Product.objects.filter(product_shop_id=request.user.shopregistration.id)
    context = {'products': products}
    return render(request, 'product/product_list.html', context)


@login_required
@user_passes_test(lambda u: u.is_seller, login_url='/seller/user-register/')
def update_product_info(request, pk):
    product = Product.objects.get(pk=pk)
    # POST METHODS
    if request.method == 'POST':

        if product.product_sub_category.subcategory_name == 'Mobiles':
            try:
                postForm = MobileSpecificationForm(request.POST,
                                                   instance=MobileSpecification.objects.get(product_id=pk))
            except MobileSpecification.DoesNotExist:
                postForm = MobileSpecificationForm(request.POST)

            if postForm.is_valid():
                obj = postForm.save(commit=False)
                obj.product = product
                obj.save()
                return redirect('product_info_update', pk)
            else:
                return HttpResponse('err')

        elif product.product_sub_category.subcategory_name == 'Laptops':
            try:
                postForm = LaptopSpecificationForm(request.POST, instance=Laptop.objects.get(product_id=pk))
            except Laptop.DoesNotExist:
                postForm = LaptopSpecificationForm(request.POST)

            if postForm.is_valid():
                obj = postForm.save(commit=False)
                obj.product = product
                obj.save()
                return redirect('product_info_update', pk)
            else:
                return HttpResponse('err')

    # GET METHODS
    else:

        if product.product_sub_category.subcategory_name == 'Mobiles':
            try:
                getForm = MobileSpecificationForm(instance=MobileSpecification.objects.get(product_id=pk))
            except MobileSpecification.DoesNotExist:
                getForm = MobileSpecificationForm()

            context = {
                'form': getForm,
                'id': pk,
            }
            return render(request, 'product/product_info_update.html', context)

        if product.product_sub_category.subcategory_name == 'Laptops':
            try:
                getForm = LaptopSpecificationForm(instance=Laptop.objects.get(product_id=pk))
            except Laptop.DoesNotExist:
                getForm = LaptopSpecificationForm()

            context = {
                'form': getForm,
                'id': pk,
            }
            return render(request, 'product/product_info_update.html', context)
