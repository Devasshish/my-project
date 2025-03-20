from django import forms
from django.contrib.auth.forms import UserCreationForm,SetPasswordForm
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserProfile
        fields = UserCreationForm.Meta.fields + ('bio', 'profile_image','email')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image', 'first_name', 'last_name', 'mobile_no', 'email', 'birth_date', 'country']


from django import forms

class ForgotPasswordForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    new_password = forms.CharField(widget=forms.PasswordInput, required=True)

class ResetPasswordForm(SetPasswordForm):
    class Meta:
        model = UserProfile
        fields = ('new_password1', 'new_password2')

from django import forms

class DeleteAccountForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())