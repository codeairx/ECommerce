from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *


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


def product_list(request):
    products = Product.objects.filter(product_shop_id=request.user.shopregistration.id)
    context = {'products': products}
    return render(request, 'product/product_list.html', context)


def update_product_info(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        if product.product_sub_category.subcategory_name == 'Mobiles':
            form = MobileSpecificationForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.product = pk
                obj.save()
                return HttpResponse('updated')
            else:
                return HttpResponse('err')
    else:
        if product.product_sub_category.subcategory_name == 'Mobiles':
            form = MobileSpecificationForm()
            context = {
                'form': form,
                'id': pk,
            }
            return render(request, 'product/mobileform.html', context)
        pass
