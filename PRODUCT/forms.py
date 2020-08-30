from django import forms
from .models import *


class StokeUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['product_shop', 'is_product_live']


class MobileSpecificationForm(forms.ModelForm):
    class Meta:
        model = MobileDetails
        fields = '__all__'
        exclude = ['product']


class PhoneChargerForm(forms.ModelForm):
    class Meta:
        model = PhoneCharger
        fields = '__all__'
        exclude = ['product']


class LaptopSpecificationForm(forms.ModelForm):
    class Meta:
        model = LaptopDetails
        fields = '__all__'
        exclude = ['product']


class LaptopChargerForm(forms.ModelForm):
    class Meta:
        model = LaptopCharger
        fields = '__all__'
        exclude = ['product']


class EarphoneForm(forms.ModelForm):
    class Meta:
        model = Earphones
        fields = '__all__'
        exclude = ['product']


class PendriveForm(forms.ModelForm):
    class Meta:
        model = Pendrive
        fields = '__all__'
        exclude = ['product']


class MemoryCardForm(forms.ModelForm):
    class Meta:
        model = MemoryCard
        fields = '__all__'
        exclude = ['product']


class SpeakerForm(forms.ModelForm):
    class Meta:
        model = Speaker
        fields = '__all__'
        exclude = ['product']


class PowerBankForm(forms.ModelForm):
    class Meta:
        model = PowerBank
        fields = '__all__'
        exclude = ['product']


class MouseForm(forms.ModelForm):
    class Meta:
        model = Mouse
        fields = '__all__'
        exclude = ['product']


class KeyboardForm(forms.ModelForm):
    class Meta:
        model = Keyboard
        fields = '__all__'
        exclude = ['product']
