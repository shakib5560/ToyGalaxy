from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, 'accounts/login-register.html')

def accounts(request):
    return render(request, 'accounts/my-account.html')