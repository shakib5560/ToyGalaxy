from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # We're using username here because Django's authenticate method uses it as the default kwarg,
        # but in our view we will pass the email as the 'username' kwarg or explicitly as 'email' depending on usage.
        # But wait, our custom User model has USERNAME_FIELD = 'email', so Django's built-in forms 
        # might pass 'username' containing the email, or 'email' directly.
        email = kwargs.get('email', username)
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None
            
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
