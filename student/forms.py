from django import forms
from .models import *


class StudentInfoSearch(forms.Form):
    roll = forms.IntegerField()


class StudentCreateForm(forms.ModelForm):

    class Meta:
        model = StudentDetail
        fields = ('name', 'roll', 'gender', 'department', 'gpa')


        GENDER_CHOICE = (
            ('male', 'Male'),
            ('female', 'Female'),
        )

        DEPT_CHOICE = (
            ('cse', 'CSE'),
            ('bba', 'BBA'),
        )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'roll': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(choices=GENDER_CHOICE, attrs={'class': 'form-control'}),
            'department': forms.Select(choices=DEPT_CHOICE, attrs={'class': 'form-control'}),
            'gpa': forms.NumberInput(attrs={'class': 'form-control'}),
        }

