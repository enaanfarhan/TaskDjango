from django import forms


class StudentInfoSearch(forms.Form):
    std_class = forms.IntegerField()
    roll = forms.IntegerField()