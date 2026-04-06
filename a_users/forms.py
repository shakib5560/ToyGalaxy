from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

User = get_user_model()

class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'username')

class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='Email / Username', widget=forms.TextInput(attrs={'autofocus': True}))
