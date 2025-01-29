from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Blog, comments, tag, Subscribe
from django.utils.text import slugify
from django.db.models import F

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'date_posted', 'images')  # Add other fields as needed
    search_fields = ('title', 'content')  # Add fields for search
    prepopulated_fields = {'slug': ('title',)}  # Automatically populate the slug based on the title
    
    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.title)  # Automatically set the slug based on the title
        super().save_model(request, obj, form, change)

# admins.py
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('blog', 'name', 'email', 'date_posted', 'isApproved')  # Include 'isApproved' here
    list_editable = ('isApproved',)  # Make 'isApproved' editable
    search_fields = ('name', 'email', 'content')
    
    def is_approved_display(self, obj):
        return obj.isApproved
    is_approved_display.boolean = True  # Optional, for boolean icons
    is_approved_display.short_description = "Approved Status"  # Optional, custom display name


class tagAdmin(admin.ModelAdmin):
    list_display = ('blog', 'title')
    search_fields = ('title',)    

class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_subscribed')
    search_fields = ('email',)    

# Registering the models with custom admin interfaces
admin.site.register(Blog, BlogAdmin)
admin.site.register(comments, CommentsAdmin)
admin.site.register(tag, tagAdmin)
admin.site.register(Subscribe, SubscribeAdmin)
