from django.shortcuts import render
from .models import *


# Create your views here.
def product_list(request):
    pro_list = product.objects.all()
    context = {'pro_list': pro_list}
    return render(request, 'Store/ProductList.html', context)

def category_list(request):
    cat_list = Category.objects.all()
    context = {'cat_list':cat_list}
    return render(request, 'Store/ProductList.html', context)

def single_product(request, id):
    single_prod = product.objects.get(id=id)
    return render(request, 'Store/SingleProduct.html', {'single_prod':single_prod})