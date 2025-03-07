from django.urls import path
from .views import search_users  # Ensure this import exists
from django.contrib.auth import views as auth_views
from .views import register, profile, logout_view, user_profile,logout_view
from .views import register, profile, user_profile, follow_user, unfollow_user, logout_view
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, profile, user_profile, follow_user, unfollow_user,search_users
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
    path('follow/<str:username>/', views.follow_user, name='follow_user'),
    path('unfollow/<str:username>/', views.unfollow_user, name='unfollow_user'),
    path('search/', search_users, name='search_users'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)