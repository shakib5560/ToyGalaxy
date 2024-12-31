from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("productdetails/<slug:slug>/", views.product_details_view, name="productdetails"),
]
