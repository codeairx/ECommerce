from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('HOME.urls')),
    path('admin/', admin.site.urls),
    path('root/', include('ADMIN.urls')),
    path('staff/', include('STAFF.urls')),
    path('account/', include('ACCOUNTS.urls')),
    path('seller/', include('SELLER.urls')),
    path('user/', include('USER.urls')),
    path('product/', include('PRODUCT.urls')),

    # PASSWORD RESET URLS
    path(
        'account/password-reset/',
        auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html'),
        name='reset_password'
    ),

    path(
        'account/password-reset-done/',
        auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
        name='password_reset_done'
    ),

    path(
        'account/password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset_confirm_view.html'),
        name='password_reset_confirm'
    ),

    path(
        'account/password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset_complete_view.html'),
        name='password_reset_complete'
    )

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
