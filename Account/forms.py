from django import forms
from .models import *

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'User Name', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

