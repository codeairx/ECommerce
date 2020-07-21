from django import forms
from .models import ShopRegistration


class ShopRegistrationForm(forms.ModelForm):
    class Meta():
        model = ShopRegistration
        fields = [
            'shop_name',
            'shop_type',
            'shop_description',
            'shop_email_address',
            'shop_address',
            'shop_state',
            'shop_city',
            'shop_pincode',
        ]
