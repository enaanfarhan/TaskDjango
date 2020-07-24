from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def add_list(request):
    add_list = Address.objects.all()
    context = {'add_list': add_list}
    return render(request, 'Address/AddressList.html', context)


def add_detalis(request, id):
    add_detalis = Address.objects.get(id=id)
    context = {'add_detalis': add_detalis}
    return render(request, 'Address/AddressDetalis.html', context)

def create_address(request):
    form = CreateAddress(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('add-list')

    context = {
            'form': form
    }
    return render(request, 'Address/CreateAddress.html', context)