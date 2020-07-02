from django.shortcuts import render
from .models import Address

# Create your views here.
def add_list(request):
    add_list = Address.objects.all()
    context = {'add_list': add_list}
    return render(request, 'Address/AddressList.html', context)


def add_detalis(request, id):
    add_detalis = Address.objects.get(id=id)
    context = {'add_detalis': add_detalis}
    return render(request, 'Address/AddressDetalis.html', context)