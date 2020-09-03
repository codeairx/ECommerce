from django.shortcuts import render
from .models import CarouselImage
from PRODUCT.models import *


def homepage(request):
    images = CarouselImage.objects.all()
    new_products = Product.objects.filter(is_product_live=True).order_by('-product_add_datetime_stamp')[:10]
    context = {
        'carousel_img': images,
        'products': new_products,
    }
    return render(request, 'home/homepage.html', context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    details = product_all_info(product.product_type, pk)
    product_images = ProductImages.objects.filter(product_id__exact=pk)
    context = {
        'product_images': product_images,
        'product': product,
        'details': details,
    }
    return render(request, 'product/product_details.html', context)


def product_all_info(productType, pk):
    data = None
    if productType == 'Smart Phones':
        data = MobileDetails.objects.get(product_id__exact=pk)

    elif productType == 'Laptop':
        data = LaptopDetails.objects.get(product_id__exact=pk)

    elif productType == 'Phone Charger':
        data = PhoneCharger.objects.get(product_id__exact=pk)

    elif productType == 'Laptop Charger':
        data = LaptopCharger.objects.get(product_id__exact=pk)

    elif productType == 'Earphone':
        data = Earphones.objects.get(product_id__exact=pk)

    elif productType == 'Power Bank':
        data = PowerBank.objects.get(product_id__exact=pk)

    elif productType == 'Pen Drive':
        data = Pendrive.objects.get(product_id__exact=pk)

    return data
