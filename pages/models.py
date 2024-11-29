from django.db import models

from django.db import models

class OfferImage(models.Model):
    image = models.ImageField(upload_to='images/', default='assets/img/slider/3.png')

    def __str__(self):
        return f'Offer Image: {self.image.name}'
    

class products(models.Model):
    Delivery_CHOICES = [
        ('free', 'Free Delivery'),
        ('standard', 'Standard Delivery'),
        ('qualified', 'Qualified Delivery'),
    ]
    CATEGORY_CHOICES = [
        ('dress', 'Baby Dress'),
        ('toy', 'Baby Toys'),
    ]
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    Delivery = models.CharField(
        max_length=500,
        choices=Delivery_CHOICES,
        default='standard',  # Default category, change as necessary
    )
    category = models.CharField(
        max_length=500,
        choices=CATEGORY_CHOICES,
        default='dress',  # Default category, change as necessary
    )

    def __str__(self):
        return f'Product: {self.name} Product Id: {self.id}'
    
    