from django.shortcuts import render
from ecommerch import models

# Create your views here.

def product_details_view(request, slug):
    product = models.Product.objects.get(slug=slug, status='Published')
    related_products = models.Product.objects.filter(category=product.category, status='Published').order_by('-id')
    context = {
        'product': product,
        'related_products': related_products,
        'range': range,  # Add the range function to the context
    }
    return render(request, 'pages/show_product.html', context)