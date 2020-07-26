from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import UserProfile


def user_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=UserProfile.objects.get(user=request.user))
        if form.is_valid():
            form.save()
            return redirect('homepage')
        else:
            return HttpResponse('err')
    else:
        print(request.user)
        form = ProfileForm(instance=UserProfile.objects.get(user=request.user))
        return render(request, 'user/profile.html', {'form': form})
