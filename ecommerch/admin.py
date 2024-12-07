from django.contrib import admin
from .models import (
    OfferImage, Category, Tag, Product, Varient, VarientItem,
    GalaryImage, Cart, Coupon, Order, OrderNote, reviews_product, setdelevaryfees
)

# Inline models
class VarientInline(admin.TabularInline):
    model = Varient
    extra = 0

class VarientItemInline(admin.TabularInline):
    model = VarientItem
    extra = 0

class GalaryImageInline(admin.TabularInline):
    model = GalaryImage
    extra = 0

class setdelevaryfeesInline(admin.TabularInline):
    model = setdelevaryfees
    extra = 0

class TagFildsInline(admin.TabularInline):
    model = Tag
    extra = 5
# Admin models

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'category', 'price', 'offer',
        'stock_quantity', 'status', 'created_at', 'hidden_price'
    ]
    list_filter = ['status', 'category']
    search_fields = ['name', 'category__name', 'tag__tag']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [GalaryImageInline, VarientInline, setdelevaryfeesInline, TagFildsInline]
    
@admin.register(OfferImage)
class OfferImageAdmin(admin.ModelAdmin):
    list_display = ['image']
    search_fields = ['image']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image']
    list_editable = ['image']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['tag']
    search_fields = ['tag']


@admin.register(Varient)
class VarientAdmin(admin.ModelAdmin):
    list_display = ['product', 'name', 'price', 'stock_quantity', 'status']
    list_filter = ['status']
    search_fields = ['product__name', 'name']
    inlines = [VarientItemInline]

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'qty', 'price', 'total', 'date']
    search_fields = ['user__username', 'product__name']

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'valid_from', 'valid_to', 'discount', 'active']
    list_filter = ['active']
    search_fields = ['code']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'user', 'total_items', 'total_amount', 'payment_status', 'date_created']
    list_filter = ['payment_status']
    search_fields = ['order_id', 'user__username']

@admin.register(OrderNote)
class OrderNoteAdmin(admin.ModelAdmin):
    list_display = ['order', 'note', 'created_at']
    search_fields = ['order__order_id']

@admin.register(reviews_product)
class ReviewsProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating', 'created_at']
    list_filter = ['rating']
    search_fields = ['product__name', 'user__username']
