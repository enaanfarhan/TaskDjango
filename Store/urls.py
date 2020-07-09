from django.urls import path
from .views import *


urlpatterns = [
    path('', store_list, name='store'),

]
