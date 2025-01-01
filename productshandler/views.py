from django.shortcuts import render, get_object_or_404, redirect
from ecommerch import models
from django.contrib import messages

def product_details_view(request, slug):
    product = get_object_or_404(models.Product, slug=slug, status='Published')
    related_products = models.Product.objects.filter(category=product.category, status='Published').order_by('-id')
    reviews = models.reviews_product.objects.filter(product=product).order_by('-created_at')
    rating_choices = models.RATING

    if request.method == "POST":
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        if request.user.is_authenticated:
            models.reviews_product.objects.create(
                product=product,
                user=request.user,
                rating=rating,
                comment=comment,
            )
            messages.success(request, "Your review has been submitted.")
            return redirect('productdetails', slug=slug)
        else:
            messages.error(request, "You need to log in to submit a review.")
            return redirect('login')

    context = {
        'product': product,
        'related_products': related_products,
        'reviews': reviews,
        'rating_choices': rating_choices,
        'range': range,
    }
    return render(request, 'pages/show_product.html', context)
