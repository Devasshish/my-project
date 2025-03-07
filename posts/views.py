from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count
from .models import Post, Like, Comment
from .forms import PostForm, CommentForm
from accounts.models import UserProfile

User = get_user_model()

@login_required
def home(request):
    posts = Post.objects.all().annotate(like_count=Count('likes')).order_by('?')
    comment_form = CommentForm()
    return render(request, 'posts/home.html', {'posts': posts, 'comment_form': comment_form})

def about(request): 
    return render(request, 'posts/about.html') 
def setting(request): 
    return render(request, 'posts/setting.html') 

def contact(request): 
    return render(request, 'posts/contact.html') 

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.like_count = 0
            post.comment_count = 0
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if not created:
        like.delete()
        liked = False
    else:
        liked = True

    return JsonResponse({'liked': liked, 'like_count': post.likes.count()})
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            
            parent_id = request.POST.get('parent_id')
            if parent_id and Comment.objects.filter(id=parent_id).exists():
                comment.parent = Comment.objects.get(id=parent_id)
            
            comment.save()

            # Get updated comment count
            updated_comment_count = post.comments.count()

            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'status': 'success',
                    'comment_id': comment.id,
                    'user': comment.user.username,
                    'content': comment.content,
                    'created_at': comment.created_at.strftime('%B %d, %Y, %I:%M %p'),
                    'comment_count': updated_comment_count  # Return updated comment count
                })
            
            return redirect('home')

    return redirect('home')

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    if request.user == comment.user:
        comment.delete()
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'status': 'success'})
    
    return redirect('home')


def help(request):
    return render(request, 'help.html')


from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Post, Comment, Like, SavedPost
from accounts.models import UserProfile

@login_required
def save_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    saved_post, created = SavedPost.objects.get_or_create(user=request.user, post=post)
    
    if not created:
        saved_post.delete()
        saved = False
    else:
        saved = True
    
    return JsonResponse({'saved': saved})




@login_required
def saved_posts(request):
    saved_posts = SavedPost.objects.filter(user=request.user)
    return render(request, 'posts/saved_posts.html', {'saved_posts': saved_posts})

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Post, SavedPost

@login_required
def unsave_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    saved_post = SavedPost.objects.filter(user=request.user, post=post)

    if saved_post.exists():
        saved_post.delete()
    
    return redirect('saved_posts')  # Redirects to the saved posts page

