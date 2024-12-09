from django.contrib import admin
from .models import Blog, Comment

class commentInline(admin.TabularInline):
    model = Comment
    extra = 1

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'profile', 'full_name', 'avatar', 'created_at', 'updated_at']
    list_filter = ['title',]
    inlines = [commentInline]

    # Define the method to display full_name
    def full_name(self, obj):
        return obj.full_name  # Calls the 'full_name' property in Blog

    # Define the method to display avatar
    def avatar(self, obj):
        return obj.avatar  # Calls the 'avatar' property in Blog

    full_name.admin_order_field = 'profile__full_name'  # Allows sorting by full_name
    avatar.admin_order_field = 'profile__avatar'  # Allows sorting by avatar

    # Optionally, you can make sure the 'full_name' and 'avatar' are not editable
    full_name.short_description = 'Full Name'
    avatar.short_description = 'Avatar'
