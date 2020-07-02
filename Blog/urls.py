from django.urls import path
from .views import *


urlpatterns=[
    path('list/', blog_list, name="blog-list"),
    path('<int:id>/', blog_post, name="blog-post")

]