from django import forms
from .models import StudentDetail


class StudentInfoSearch(forms.Form):
    std_class = forms.IntegerField()
    roll = forms.IntegerField()


class StudentCreateForm(forms.ModelForm):

    class Meta:
        model = StudentDetail
        exclude = ('gpa',)

        GENDER_CHOICE = (
            ('male', 'Male'),
            ('female', 'Female'),
        )

        widgets = {
            'roll': forms.NumberInput(attrs={'class':'form-control'}),
            'name': forms.Textarea(attrs={'class':'form-control'}),
            'gender': forms.Select(choices=GENDER_CHOICE, attrs={'class':'form-control'}),
            'department': forms.Textarea(attrs={'class':'form-control'}),
            'std_class': forms.NumberInput(attrs={'class':'form-control'}),
        }