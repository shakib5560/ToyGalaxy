from django.shortcuts import render

def home(request):
    return render(request, 'pages/index.html')
# Create your views here.

def shop(request):
    return render(request, 'pages/shop.html', {'my_range': range(1, 20)})

def cart(request):
    return render(request, 'pages/shop-cart.html')

def checkout(request):
    return render(request, 'pages/shop-checkout.html')

def blog(request):
    return render(request, 'pages/blog.html', {'my_range': range(1, 20)})

def wishlist(request):
    return render(request, 'pages/wishlist.html', {'my_range': range(1, 20)})

def blog_details(request):
    return render(request, 'pages/blog-details.html')
