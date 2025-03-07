from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post

@login_required
def home(request):
    posts = Post.objects.all()
    return render(request, 'posts/home.html', {'posts': posts})
