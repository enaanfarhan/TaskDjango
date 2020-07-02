from django.shortcuts import render
from .models import *

# Create your views here.
def blog_list(request):
    blog_list = blog.objects.all()
    context = {'blog_list':blog_list}
    return render(request, 'Blog/BlogList.html', context)

def blog_post(request, id):
    blog_post = blog.objects.get(id=id)
    context = {'blog_post': blog_post}
    return render(request, 'Blog/BlogPost.html', context)