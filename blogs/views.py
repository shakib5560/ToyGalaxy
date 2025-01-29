from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, tag, Subscribe, comments
from django.contrib import messages 

def blog(request):
    blogs = Blog.objects.order_by('-id')[:8]
    return render(request, 'pages/blog.html', {'blogs': blogs})

def blog_details(request, slug):
    blogs = get_object_or_404(Blog, slug=slug)
    allblogs = Blog.objects.order_by('-id')[:4]
    tags = tag.objects.filter(blog=blogs).order_by('-id')[:5]
    comment = comments.objects.filter(blog=blogs, isApproved = True).order_by('-id')

    if request.method == 'POST':
        # Handle subscription
        if 'subscribe' in request.POST:
            email = request.POST.get('email')
            if email:
                Subscribe.objects.create(email=email)
                messages.success(request, "You have successfully subscribed!")
                return redirect('blog-details', slug=slug)

        # Handle comment submission
        if 'comment' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            content = request.POST.get('content')

            if name and email and content:
                comments.objects.create(blog=blogs, name=name, email=email, content=content)
                messages.success(request, "Your comment has been submitted! It will be approved shortly.")
            else:
                messages.error(request, "Please fill out all required fields.")
            return redirect('blog-details', slug=slug)

    context = {
        'blogs': blogs,
        'allblogs': allblogs,
        'tags': tags,
        'comment': comment,
    }
    return render(request, 'pages/blog-details.html', context)
