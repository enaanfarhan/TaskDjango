from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def user_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('logingit pull')
    return render(request, 'Account/dashboard.html')

def user_login(request):
    form = UserLoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
            context = {
                'form': form,
                'error': "Sorry! no user found!!!"
            }
            return render(request, 'Account/login.html', context)


    context = {
        'form': form
    }
    return render(request, 'Account/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('login')


def user_register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {
        'form':form
    }
    return render(request, 'Account/register.html', context)

