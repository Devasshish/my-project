from django.contrib import admin
from .models import Post, Like, Comment, SavedPost

class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'caption', 'created_at', 'get_like_count', 'get_comment_count')

    def get_like_count(self, obj):
        return obj.get_like_count()
    get_like_count.short_description = 'Likes'

    def get_comment_count(self, obj):
        return obj.get_comment_count()
    get_comment_count.short_description = 'Comments'

class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'content', 'created_at')

class SavedPostAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at')

admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(SavedPost, SavedPostAdmin)
from .models import ContactSubmission

from django.contrib import admin
from .models import ContactSubmission

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)