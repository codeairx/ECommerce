from django.shortcuts import render
from .models import CarouselImage
from PRODUCT.models import Product


def homepage(request):
    images = CarouselImage.objects.all()
    new_products = Product.objects.filter(is_product_live=True).order_by('-product_add_datetime_stamp')[:10]
    context = {
        'carousel_img': images,
        'products': new_products,
    }
    return render(request, 'home/homepage.html', context)
