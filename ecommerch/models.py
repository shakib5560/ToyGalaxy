from django.db import models
from django.core.files.base import ContentFile
from shortuuid.django_fields import ShortUUIDField
from django.utils import timezone
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg

from a_users import models as user_models


import requests
import uuid

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
    slug = slug = models.SlugField(unique=True, null=True, blank=True)   # To make url seo friendly 
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f'Category: {self.name}'

    class Meta:
        verbose_name_plural = 'Categories'
        


# Product Models
class Product(models.Model):
    name = models.CharField(max_length=500)
    slug = models.SlugField(unique=True, null=True, blank=True)   # To make url seo friendly 
    
    #Price Fields
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00, verbose_name='Sale Price', null=True, blank=True)
    offer = models.DecimalField(decimal_places=2, max_digits=10, default=0.00, verbose_name='Offer Price', null=True, blank=True)
    hidden_price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00, verbose_name='Overall Price', null=True, blank=True)

     
    #Others
    image = models.ImageField(upload_to='product_images/')
    description = models.TextField(max_length=2000, null=True, blank=True)
    Delivery = models.CharField(choices=[('free', 'Free Delivery'), ('standard', 'Standard Delivery'), ('qualified', 'Qualified Delivery')], default='standard', max_length=500)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    support_24_7 = models.BooleanField(default=True)
    money_return = models.BooleanField(default=True)
    sku = ShortUUIDField(unique=True, length=5, max_length=20, prefix='SKU', alphabet='1234567890')
    status = models.CharField(choices=STATUS, default='Published', max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stock_quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return f'Product: {self.name}'
    
    def average_rating(self):
        result = reviews_product.objects.filter(product=self).aggregate(avg_rating=Avg('rating'))
        return result['avg_rating'] or 0  # Return 0 if there are no ratings
    
    def reviews(self):
        return reviews_product.objects.filter(product=self)

    
    class Meta:
        verbose_name_plural = 'Products'
        ordering = ['-created_at']


# varient models
class Varient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=300, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00, verbose_name='Sale Price', null=True, blank=True)
    offer = models.DecimalField(decimal_places=2, max_digits=10, default=0.00, verbose_name='Offer Price', null=True, blank=True)
    overallprice = models.DecimalField(decimal_places=2, max_digits=10, default=0.00, verbose_name='Overall Price', null=True, blank=True)
    stock_quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(choices=STATUS, default='Published', max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Varient: {self.name}'

    def titlesave(self, *args, **kwargs):
        if not self.name:
            self.name = self.product.name
        if not self.price:
            self.price = self.product.price
        if not self.offer:
            self.offer = self.product.offer
        if not self.overallprice:
            self.overallprice = self.product.overallprice
        if not self.stock_quantity:
            self.stock_quantity = self.product.stock_quantity
        if not self.status:
            self.status = self.product.status                        
        super(Varient, self).save(*args, **kwargs)    


#varient item models
class VarientItem(models.Model):
    varient = models.ForeignKey(Varient, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    content = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'VarientItem: {self.name}'
    
class GalaryImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    alt_tag = models.CharField(max_length=500, null=True, blank=True) 

    def defaultalttag(self):
        if not self.alttag:
           self.alttag = self.product.name

    def __str__(self):
        return f'GalaryImage: {self.galary_id}'
    

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(user_models.User, on_delete=models.SET_NULL, null=True, blank=True)
    qty = models.PositiveIntegerField(default=0, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=12, default=0.00, null=True, blank=True)
    sub_total = models.DecimalField(decimal_places=2, max_digits=12, default=0.00, null=True, blank=True)
    shipping = models.DecimalField(decimal_places=2, max_digits=12, default=0.00, null=True, blank=True)
    tax = models.DecimalField(decimal_places=2, max_digits=12, default=0.00, null=True, blank=True)
    total = models.DecimalField(decimal_places=2, max_digits=12, default=0.00, null=True, blank=True)
    size = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)
    cart_id = models.CharField(max_length=1000, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cart_id} - {self.product.name}'


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code
    

# Order models

class Order(models.Model):
    # ForeignKey to the User model
    user = models.ForeignKey(
        user_models.User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="The user who placed the order"
    )
    # ForeignKey to the UserProfile model
    userprofile = models.ForeignKey(
        user_models.UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="The profile details of the user"
    )
    # Additional fields related to the order
    order_id = models.CharField(
        primary_key=True, 
        default=uuid.uuid4().hex[:5].upper(), 
        max_length=50, 
        editable=False
    )

    total_items = models.PositiveIntegerField(
        default=0,
        help_text="The total number of items in the order"
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        help_text="The total amount for the order"
    )

    payment_status = models.CharField(
        max_length=50,
        choices=[
            ("Pending", "Pending"),
            ("Paid", "Paid"),
            ("Failed", "Failed"),
        ],
        default="Pending",
        help_text="The payment status of the order"
    )

    shipping_address = models.CharField(
        max_length=250,
        blank=True,
        null=True,
        help_text="Shipping address provided during checkout"
    )

    apply_coupon = models.BooleanField(
        default=False,
        help_text="Whether a coupon was applied during checkout"
    )

    tax = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        help_text="The tax amount for the order"
    )

    shipping = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        help_text="The shipping amount for the order"
    )

    date_created = models.DateTimeField(
        default=timezone.now,
        help_text="The date and time when the order was created"
    )

    def save(self, *args, **kwargs):
        # Automatically set the userprofile if user is provided
        if self.user and not self.userprofile:
            try:
                self.userprofile = user_models.UserProfile.objects.get(user=self.user)
            except user_models.UserProfile.DoesNotExist:
                pass  # Leave userprofile as None if no UserProfile exists
            
        # Set default values for fields not in UserProfile
        if not self.shipping_address and self.userprofile:
            self.shipping_address = f"{self.userprofile.address}, {self.userprofile.city}, {self.userprofile.state}, {self.userprofile.zip_code}"

        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.order_id} by {self.user.username if self.user else 'Unknown'}"

    @property
    def full_shipping_address(self):
        if self.shipping_address:
            return self.shipping_address
        return "No shipping address provided"


# Example of another model, e.g., Notes for Orders
class OrderNote(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="notes"
    )
    note = models.TextField(
        help_text="Any special notes or instructions for this order"
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        help_text="The date and time when the note was created"
    )

    def __str__(self):
        return f"Note for Order {self.order.order_id}"


class reviews_product(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=RATING, null=True, blank=True, default=None)
    comment = models.TextField(null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    reply = models.TextField(null=True, blank=True, default=None)

    def __str__(self):
        return f"Review for {self.product.name} by {self.user.username}"
    
    class Meta:
        verbose_name_plural = "Reviews"
    

class setdelevaryfees(models.Model):
    standard_delivery = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    qualified_delivery = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    product = models.OneToOneField(on_delete=models.SET_NULL, null=True, blank=True, to=Product)    

    def __str__(self):
        return f"Delivery Fees for {self.product.name}"
     

# HElP ITS FOR SEO
class Tag(models.Model):
    tags_products = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    tag = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f' SEO Tag: {self.tag}'