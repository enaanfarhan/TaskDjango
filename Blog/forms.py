from django import forms
from .models import *

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = ('title', 'slug', 'description', 'author', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(),
        }

class CreateAuthor(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }