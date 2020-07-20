from django.contrib.auth import authenticate
from django.shortcuts import render
from .forms import *

# Create your views here.
def user_login(request):
    form = UserLoginForm()
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            authenticate()


    context ={'form':form}
    return render(request, 'Account/login.html', context)
