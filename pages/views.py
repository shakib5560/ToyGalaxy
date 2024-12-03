from django.shortcuts import render
from .models import OfferImage

def home(request):
    # Retrieve the most recent image uploaded
    latest_image = OfferImage.objects.order_by('-id').first()  # Order by ID to get the latest one
    return render(request, 'pages/index.html', {'latest_image': latest_image})
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