from django.urls import path
from .views import *

urlpatterns = [
    path('login/', user_login, name="login"),
    path('dashboard/', user_dashboard, name="dashboard"),
    path('logout/', user_logout, name="logout"),
    path('register/', user_register, name="register")

]