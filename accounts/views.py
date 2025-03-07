from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from .forms import CustomUserCreationForm, UserProfileForm  # Correct imports
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserProfile


def logout_view(request):
    auth_logout(request)
    return redirect('login')

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to refresh the profile page
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'accounts/profile.html', {'form': form})
    # def register(request):
    #     if request.method == 'POST':
    #         form = CustomUserCreationForm(request.POST, request.FILES)
    #         if form.is_valid():
    #             user = form.save()
    #             username = form.cleaned_data.get('username')
    #             password = form.cleaned_data.get('password1')
    #             user = authenticate(username=username, password=password)
    #             login(request, user)
    #             return redirect('home')
    #     else:
    #         form = CustomUserCreationForm()
    #     return render(request, 'accounts/register.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            if not user.email:  # If email is empty
                user.email = None  # Set email to None to avoid empty string duplicates
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


from django.shortcuts import render, get_object_or_404
from .models import UserProfile

from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Follow

@login_required
def user_profile(request, username):
    profile_user = get_object_or_404(UserProfile, username=username)
    is_following = Follow.objects.filter(follower=request.user, following=profile_user).exists()
    followers_count = Follow.objects.filter(following=profile_user).count()
    following_count = Follow.objects.filter(follower=profile_user).count()
    posts = profile_user.posts.all()  # ✅ Fixed: Use 'posts' instead of 'post_set'
    
    return render(request, 'accounts/user_profile.html', {
        'profile_user': profile_user,
        'is_following': is_following,
        'followers_count': followers_count,
        'following_count': following_count,
        'posts': posts
    })


from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Follow
@login_required
def follow_user(request, username):
    user_to_follow = get_object_or_404(UserProfile, username=username)
    Follow.objects.get_or_create(follower=request.user, following=user_to_follow)
    return redirect('user_profile', username=username)


@login_required
def unfollow_user(request, username):
    user_to_unfollow = get_object_or_404(UserProfile, username=username)
    Follow.objects.filter(follower=request.user, following=user_to_unfollow).delete()
    return redirect('user_profile', username=username)


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserProfile

@login_required
def search_users(request):
    query = request.GET.get('q', '')  # Changed from 'query' to 'q'
    if query:
        results = UserProfile.objects.filter(username__icontains=query)
    else:
        results = []
    return render(request, 'search.html', {
        'query': query,
        'users': results ,
       
    })
