from django import forms
from .models import Post
from django.core.exceptions import ValidationError
from django import forms
from .models import Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'caption']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'caption': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write a caption...'}),
        }

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if not image.content_type.startswith('image/'):
                raise ValidationError("Only image files are allowed.")
            if image.size > 5 * 1024 * 1024:  # 5 MB size limit
                raise ValidationError("Image size should not exceed 5 MB.")
        return image

    def clean_caption(self):
        caption = self.cleaned_data.get('caption')
        if len(caption) > 255:
            raise forms.ValidationError("Caption cannot exceed 255 characters.")
        return caption



class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Write a comment...',
            'rows': '3',
        })
    )

    class Meta:
        model = Comment
        fields = ['content']
