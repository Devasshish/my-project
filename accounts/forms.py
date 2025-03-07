from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserProfile
        fields = UserCreationForm.Meta.fields + ('bio', 'profile_image',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image', 'first_name', 'last_name', 'mobile_no', 'email', 'birth_date', 'country']
