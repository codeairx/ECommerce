from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda u: u.is_superuser, login_url='/account/login/')
def admin_login(request):
    return render(request, 'admin/admin_home.html')
