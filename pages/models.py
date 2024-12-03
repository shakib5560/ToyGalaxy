from django.db import models
from django.core.files.base import ContentFile
from shortuuid.django_fields import ShortUUIDField
from django.utils import timezone
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from autoslug import AutoSlugField

from a_users import models as user_models


import requests
import shortuuid

# Order Status
ORDER_STATUS = (
    ("Pending", "Pending"),
    ("Processing", "Processing"),
    ("Shipped", "Shipped"),
    ("Fulfilled", "Fulfilled"),
    ("Cancelled", "Cancelled"),
)

# Shipping Service
SHIPPING_SERVICE = (
    ("DHL", "DHL"),
    ("FedX", "FedX"),
    ("UPS", "UPS"),
    ("GIG Logistics", "GIG Logistics"),
)

# Rating
RATING = (
    (1, "⭐☆☆☆☆"),
    (2, "⭐⭐☆☆☆"),
    (3, "⭐⭐⭐☆☆"),
    (4, "⭐⭐⭐⭐☆"),
    (5, "⭐⭐⭐⭐⭐"),
)

# Status
STATUS = (
    ("Published", "Published"),
    ("Draft", "Draft"),
    ("Disabled", "Disabled"),
)

# Payment Status
PAYMENT_STATUS = (
    ("Paid", "Paid"),
    ("Processing", "Processing"),
    ("Failed", "Failed"),
)

# Payment Method
PAYMENT_METHOD = (
    ("PayPal", "PayPal"),
    ("Stripe", "Stripe"),
    ("Flutterwave", "Flutterwave"),
    ("Paystack", "Paystack"),
)


class OfferImage(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f'Offer Image: {self.image.name if self.image else "No Image"}'

    def save(self, *args, **kwargs):
        # Check if image is not set
        if not self.image:
            # Fetch the default image from the URL
            default_image_url = 'https://i.ibb.co/ckXK4Dq/3.png'
            response = requests.get(default_image_url)
            if response.status_code == 200:
                self.image.save(
                    'default.png',  # Name for the saved file
                    ContentFile(response.content),
                    save=False
                )
        super(OfferImage, self).save(*args, **kwargs)


# Catagory Models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title', null=True, unique=True, default=None)   # To make url seo friendly 
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f'Category: {self.name}'

    class Meta:
        verbose_name_plural = 'Categories'
        

# Tag Models
class Tag(models.Model):
    name = models.CharField(max_length=100)  # e.g., "Toys, Dress"
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name


# Product Models
class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title', null=True, unique=True, default=None)   # To make url seo friendly 
    
    #Price Fields
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00, verbose_name='Sale Price', null=True, blank=True)
    offer = models.DecimalField(decimal_places=2, max_digits=10, default=0.00, verbose_name='Offer Price', null=True, blank=True)
    overallprice = models.DecimalField(decimal_places=2, max_digits=10, default=0.00, verbose_name='Overall Price', null=True, blank=True)

     
    #Others
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    description = models.TextField(max_length=2000, )
    Delivery = models.CharField(choices=[('free', 'Free Delivery'), ('standard', 'Standard Delivery'), ('qualified', 'Qualified Delivery')], default='standard', max_length=500)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    support_24_7 = models.BooleanField(default=True)
    money_return = models.BooleanField(default=True)
    sku = models.CharField(max_length=100, unique=True)
    tag = models.ManyToManyField(Tag, blank=True)
    status = models.CharField(choices=STATUS, default='Published', max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stock_quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return f'Product: {self.name}'

    
    class Meta:
        verbose_name_plural = 'Products'


    
    