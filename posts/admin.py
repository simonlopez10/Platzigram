"""Post admin classes"""
# Django
from django.contrib import admin
#Models
from posts.models import Post

# Register your models here.
@admin.register(Post)
class ProfileAdmin(admin.ModelAdmin):
    """Post admin."""
    
    list_display = ('id', 'user', 'title', 'photo')
    search_fields = ('title', 'user__username', 'user__email')
    list_filter = ('created', 'modified')