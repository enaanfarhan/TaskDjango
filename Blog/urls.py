from django.urls import path
from .views import *


urlpatterns=[
    path('list/', blog_list, name="blog-list"),
    path('<int:id>/', blog_post, name="blog-post"),
    path('authors/', author_list, name="authors"),
    path('authors/<author_name>', author_post),
]