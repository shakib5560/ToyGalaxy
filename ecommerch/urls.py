from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('shop/', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('show-product/', views.show_product, name='show-product'),
    path('product-details/<slug:slug>/', views.product_details_view, name='product_details'),
    path('items/', include('productshandler.urls')),
]
