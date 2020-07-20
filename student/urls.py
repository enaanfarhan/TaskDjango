from django.urls import path
from .views import *


urlpatterns = [
    path('list/', std_list, name='std-list'),
    path('<int:roll>/', std_info, name='std-info'),
    path('search/', std_search, name='std-search'),
    path('create/', addStudent, name='create-std'),
]
