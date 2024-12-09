from django.db import models
from a_users.models import User, UserProfile
from ckeditor.fields import RichTextField

class Blog(models.Model):
    profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    images = models.ImageField(upload_to='images/', blank=True, null=True)
    content = RichTextField(max_length=2000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def full_name(self):
        return self.profile.full_name if self.profile else "N/A"
    
    @property
    def email(self):
        return self.profile.email if self.profile else "N/A"
    
    @property
    def avatar(self):
        return self.profile.avatar.url if self.profile and self.profile.avatar else "default_avatar_url"
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.blog.title}"
       