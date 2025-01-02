from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('blog-details/<slug:slug>/', views.blog_details, name='blog-details'),
]
