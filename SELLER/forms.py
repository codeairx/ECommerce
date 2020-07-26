from django import forms
from .models import ShopRegistration, ShopOwnerRegistration, ShopOwnerBankDetails


class ShopOwnerRegisterForm(forms.ModelForm):
    class Meta:
        model = ShopOwnerRegistration
        fields = '__all__'

        widgets = {'password': forms.PasswordInput()}


class ShopRegisterForm(forms.ModelForm):
    class Meta:
        model = ShopRegistration
        fields = '__all__'


class ShopOwnerBankForm(forms.ModelForm):
    class Meta:
        model = ShopOwnerBankDetails
        fields = '__all__'


class SellerLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
