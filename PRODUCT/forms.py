from django import forms
from .models import *


class MobileSpecificationForm(forms.ModelForm):
    class Meta:
        model = MobileSpecification
        fields = '__all__'
        exclude = ['product']


class LaptopSpecificationForm(forms.ModelForm):
    class Meta:
        model = Laptop
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


class PhoneChargerForm(forms.ModelForm):
    class Meta:
        model = PhoneCharger
        fields = '__all__'
        exclude = ['product']
