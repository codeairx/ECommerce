from django import forms
from .models import ShopRegistration, ShopOwnerProfile
from django.contrib.auth.models import User


class ShopOwnerDetailsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]

    def __init__(self, *args, **kwargs):
        super(ShopOwnerDetailsForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['username'].widget.attrs['readonly'] = True
            self.fields['first_name'].widget.attrs['readonly'] = True
            self.fields['last_name'].widget.attrs['readonly'] = True
            self.fields['email'].widget.attrs['readonly'] = True


class ShopOwnerProfileForm(forms.ModelForm):
    class Meta:
        model = ShopOwnerProfile
        fields = [
            'shop_owner_contact_no',
            'shop_owner_contact_address',
            'shop_owner_PAN_no',
        ]


class ShopRegistrationForm(forms.ModelForm):
    class Meta():
        model = ShopRegistration
        fields = [
            'shop_name',
            'shop_type',
            'shop_description',
            'shop_email_address',
            'shop_address',
            'shop_pincode',
            'shop_state',
            'shop_city',
        ]
