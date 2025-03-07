from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    mobile_no = models.CharField(max_length=15, blank=True)
    email = models.EmailField(unique=True, blank=True, null=True)    
    birth_date = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=50, blank=True)

    def __str__(self):  # Fixed double underscores
        return self.username


class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(UserProfile, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')