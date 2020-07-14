from django.urls import path
from .views import *


urlpatterns = [
    path('', product_list, name="store"),
    path('<int:id>/', single_product, name="single-product"),
    path('category/<category_name>', product_category, name="category-list"),
]
