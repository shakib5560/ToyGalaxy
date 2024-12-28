from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Product, reviews_product

@receiver(post_save, sender=reviews_product)
@receiver(post_delete, sender=reviews_product)
def update_product_rating(sender, instance, **kwargs):
    if instance.product:
        instance.product.calculate_average_rating()
