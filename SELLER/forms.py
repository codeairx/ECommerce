from django import forms
from .models import ShopRegistration, ShopOwnerProfile, ShopOwnerBankDetails


class ShopOwnerProfileForm(forms.ModelForm):
    class Meta:
        model = ShopOwnerProfile
        fields = '__all__'
        exclude = ['user']

        widgets = {'password': forms.PasswordInput()}


class ShopRegisterForm(forms.ModelForm):
    class Meta:
        model = ShopRegistration
        fields = '__all__'
        exclude = ['owner', 'shop_verified']


class ShopOwnerBankForm(forms.ModelForm):
    class Meta:
        model = ShopOwnerBankDetails
        fields = '__all__'
        exclude = ['shop_owner']


class SellerLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
