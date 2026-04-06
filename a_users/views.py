from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth import get_user_model
from django.conf import settings

from .forms import UserRegisterForm, UserLoginForm

User = get_user_model()

def login_register_view(request):
    if request.user.is_authenticated:
        return redirect('index') # Redirect to home if already logged in

    login_form = UserLoginForm()
    register_form = UserRegisterForm()

    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'login':
            login_form = UserLoginForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                messages.success(request, f"Welcome back, {user.username or user.email}!")
                next_url = request.GET.get('next', 'index')
                return redirect(next_url)
            else:
                messages.error(request, "Invalid email or password.")
        
        elif form_type == 'register':
            register_form = UserRegisterForm(request.POST)
            if register_form.is_valid():
                user = register_form.save()
                # Log the user in after registration
                login(request, user)
                messages.success(request, "Registration successful. Welcome!")
                return redirect('index')
            else:
                messages.error(request, "Registration failed. Please correct the errors below.")

    context = {
        'login_form': login_form,
        'register_form': register_form
    }
    return render(request, 'accounts/login-register.html', context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "You have been logged out.")
        return redirect('login_register')
    # If GET request, redirect to home or somewhere safe
    return redirect('index')


def password_reset_request_view(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(email=data)
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "accounts/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': request.META['HTTP_HOST'],
                        'site_name': 'ToyGalaxy',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, settings.DEFAULT_FROM_EMAIL , [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
                    return redirect ("login_register")
            else:
                 messages.error(request, 'An invalid email has been entered.')
    else:
        password_reset_form = PasswordResetForm()
    return render(request=request, template_name="accounts/password-reset.html", context={"password_reset_form":password_reset_form})

def password_reset_confirm_view(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been set. You may go ahead and log in now.")
                return redirect('login_register')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
        else:
            form = SetPasswordForm(user)
        return render(request, 'accounts/password-reset-confirm.html', {'form': form})
    else:
        messages.error(request, "The password reset link was invalid, possibly because it has already been used. Please request a new password reset.")
        return redirect('password_reset_request')