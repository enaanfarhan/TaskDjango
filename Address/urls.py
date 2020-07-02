from django.urls import path
from .views import *

urlpatterns =[
    path('list/', add_list, name="add-list"),
    path('<int:id>/', add_detalis, name="add-detalis")
]