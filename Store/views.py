from django.shortcuts import render
from .models import *


# Create your views here.
def product_list(request):
    pro_list = product.objects.all()
    context = {'pro_list': pro_list}
    return render(request, 'Store/ProductList.html', context)


def product_category(request, category_name):
    cat_list = Category.objects.get(name=category_name)
    c_list = product.objects.filter(category=cat_list)
    context = {'c_list':c_list, 'name':category_name}
    return render(request, 'Store/ProductCategory.html', context)


def single_product(request, id):
    single_prod = product.objects.get(id=id)
    return render(request, 'Store/SingleProduct.html', {'single_prod':single_prod})