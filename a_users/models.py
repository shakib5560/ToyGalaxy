from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True, blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"Account: {self.username}"
    

    def save(self, *args, **kwargs):
        emain_username, _ = self.email.split('@')
        if not self.username:
            self.username = emain_username
        super(User, self).save(*args, **kwargs)   


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    housenumber = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"Profile: {self.user.username}"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def email(self):
        return self.user.email
    
    @property
    def username(self):
        return self.user.username
    
    @property
    def id(self):
        return self.user.id
    
    @property
    def date_joined(self):
        return self.user.date_joined
    
    @property
    def profile(self):
        return self.avatar if self.avatar else "https://i.pinimg.com/474x/65/25/a0/6525a08f1df98a2e3a545fe2ace4be47.jpg"
    
    def save(self, *args, **kwargs):
        notprovide = "Buyers"
        if not self.first_name:
            self.first_name = self.user.username
        if not self.last_name:
            self.last_name = notprovide     
        super(UserProfile, self).save(*args, **kwargs)

