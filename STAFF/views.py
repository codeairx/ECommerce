from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda u: u.is_staff and not u.is_superuser)
def staff_home(request):
    return render(request, 'staff/staff_home.html')
