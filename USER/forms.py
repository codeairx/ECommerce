from django import forms
from .models import UserProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'

        widgets = {
            'user': forms.HiddenInput(),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'delivery_address1': forms.Textarea(attrs={'class': 'form-control'}),
            'delivery_address2': forms.Textarea(attrs={'class': 'form-control'}),
        }
