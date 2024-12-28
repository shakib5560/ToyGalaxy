from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('shop/', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('blog/', views.blog, name='blog'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('blog-details/', views.blog_details, name='blog-details'),
    path('show-product/', views.show_product, name='show-product'),
    path('product-details/<slug:slug>/', views.product_details_view, name='product_details'),
]
