from django.shortcuts import render
from .models import Blog

def blog(request):
    blogs = Blog.objects.order_by('-id')[:8]
    return render(request, 'pages/blog.html', {'blogs': blogs})

def blog_details(request, slug):
    blogs = Blog.objects.get(slug=slug)
    return render(request, 'pages/blog-details.html', {'blogs': blogs})  
