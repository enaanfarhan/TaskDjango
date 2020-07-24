from django import forms
from .models import *

class CreateAddress(forms.ModelForm):

    class Meta:
        model = Address
        fields = ('name', 'division', 'population', 'area')

        DIVISION_CHOICE = (
            ('barisal', 'Barisal'),
            ('chittagong', 'Chittagong'),
            ('dhaka', 'Dhaka'),
            ('khulna', 'Kulna'),
            ('mymensingh', 'Mymensingh'),
            ('rajshahi', 'Rajshahi'),
            ('sylhet', 'Sylhet'),
            ('rangpur', 'Rangpur'),
        )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'division': forms.Select(choices=DIVISION_CHOICE, attrs={'class': 'form-control'}),
            'population': forms.NumberInput(attrs={'class': 'form-control'}),
            'area': forms.NumberInput(attrs={'class': 'form-control'}),
        }

