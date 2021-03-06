from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.
def author_list(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, 'Blog/AuthorList.html', context)

def author_post(request, author_name):
    a_name = Author.objects.get(name=author_name)
    aposts = blog.objects.filter(author=a_name)
    context = {'aposts': aposts, 'name': author_name}
    return render(request, 'Blog/AuthorsPost.html', context)

def blog_list(request):
    blog_list = blog.objects.all()
    context = {'blog_list': blog_list}
    return render(request, 'Blog/BlogList.html', context)

def blog_post(request, slug):
    blog_post = blog.objects.get(slug=slug)
    context = {'blog_post': blog_post}
    return render(request, 'Blog/BlogPost.html', context)


def createblogpost(request):
    form = CreatePostForm()
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog-list')
    context = {
        'form': form
    }
    return render(request, 'Blog/CreateBlogPost.html', context)

#def create_author(request):
#    form = CreateAuthor()
#    context = {
#        'form': form
#    }
#   return render(request, 'Blog/AddAuthor.html', context)

def create_author(request):
    form = CreateAuthor()
    if request.method == 'POST':
        form = CreateAuthor(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create-author')
    context = {
        'form': form
    }
    return render(request, 'Blog/AddAuthor.html', context)