from django.shortcuts import render
from .models import OfferImage, Product, Category, GalaryImage, Varient, VarientItem
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from django.db.models import Case, When
from django.db import models
from blogs.models import Blog

def home(request):
    # Fetch the latest 8 published products
    productdata = Product.objects.filter(status='Published').order_by('-id')[:16]
    categorys = Category.objects.order_by('-id')[:3]
    blogs = Blog.objects.order_by('-id')[:3]
    
    context = {
        'products': productdata,
        'categorys': categorys,
        'blogs': blogs,

    }

    # Render the template with context
    return render(request, 'pages/index.html', context)



# Create your views here.

from django.db.models import F

def shop(request):
    categories = Category.objects.all()
    sort_by = request.GET.get('sort', 'created_at')  # Default sorting by created_at

    # Apply sorting logic based on sort_by parameter
    if sort_by == 'offer':
        products = Product.objects.filter(status='Published').order_by('offer')  # Low to high
    elif sort_by == 'delivery':
        products = Product.objects.filter(status='Published').order_by(
            Case(
                When(Delivery='free', then=0),  # Prioritize free delivery
                default=1,
                output_field=models.IntegerField(),
            )
        )
    else:
        products = Product.objects.filter(status='Published').order_by('-created_at')  # Default: Most recent

    context = {
        'categories': categories,
        'products': products,
        'sort_by': sort_by,
    }

    return render(request, 'pages/shop.html', context)


def product_details_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    data = {
        "slug": product.slug,
        "name": product.name,
        "price": product.price,
        "offer": product.offer,
        "hidden_price": product.hidden_price,
        "image": product.image.url if product.image else None,
        "description": product.description,
        "delivery": product.Delivery,
        "category": str(product.category),  # Convert category to string if it's a related object
        "support_24_7": product.support_24_7,
        "money_return": product.money_return,
        "sku": product.sku,
        "status": product.status,
        "created_at": product.created_at.isoformat(),  # Convert to ISO format for JSON compatibility
        "updated_at": product.updated_at.isoformat(),
        "stock_quantity": product.stock_quantity,
        "average_rating": product.average_rating(),
    }
    return JsonResponse(data)

    

def cart(request):
    return render(request, 'pages/shop-cart.html')

def checkout(request):
    return render(request, 'pages/shop-checkout.html')

def wishlist(request):
    return render(request, 'pages/wishlist.html', {'my_range': range(1, 20)})


def show_product(request):
    return render(request, 'pages/show_product.html', {'my_range': range(1, 20)})    