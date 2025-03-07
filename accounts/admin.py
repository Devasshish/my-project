from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'bio')

admin.site.register(UserProfile, UserProfileAdmin)
