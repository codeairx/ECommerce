from django.shortcuts import render
from .models import CarouselImage


def homepage(request):
    images = CarouselImage.objects.all()
    print(images)
    context = {
        'carousel_img': images,
    }
    return render(request, 'home/homepage.html', context)
