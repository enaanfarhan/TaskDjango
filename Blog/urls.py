from django.urls import path
from .views import *


urlpatterns=[
    path('list/', blog_list, name="blog-list"),
    path('<slug>/', blog_post, name="blog-post"),
    path('authors/list', author_list, name="authors"),
    path('authors/<author_name>', author_post, name="author-post"),
]