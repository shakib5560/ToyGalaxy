from django.db import models
from ckeditor.fields import RichTextField
from a_users.models import User

# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    images = models.ImageField(upload_to='blogs', blank=True, null=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True) 
    
    content = RichTextField(null=True, blank=True)
    pointmessage = models.CharField(max_length=100, null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def tags(self):
        return tag.objects.filter(blog=self)

class comments(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField(max_length=1000, null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    reply = models.TextField(max_length=1000, null=True, blank=True, default='Thank you for your comment. We will get back to you soon.')
    isApproved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class tag(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Subscribe(models.Model):
    email = models.EmailField(null=True, blank=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


