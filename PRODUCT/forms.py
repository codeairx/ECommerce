from django import forms
from .models import *


class MobileSpecificationForm(forms.ModelForm):
    class Meta:
        model = MobileSpecification
        fields = '__all__'
        exclude = ['product']
