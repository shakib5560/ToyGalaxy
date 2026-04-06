from django.urls import path
from . import views

urlpatterns = [
    path('login-register/', views.login_register_view, name='login_register'), # Used internally in templates
    path('', views.login_register_view, name='register'), # Map the old name too just in case
    path('logout/', views.logout_view, name='logout'),
    path('password-reset/', views.password_reset_request_view, name='password_reset_request'),
    path('password-reset/<uidb64>/<token>/', views.password_reset_confirm_view, name='password_reset_confirm'),
]
