from django.urls import path
from .views import home, create_post, like_post,about,contact,add_comment,save_post,saved_posts,setting,unsave_post
from . import views
urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'), 
    path('contact/', contact, name='contact'),
    path('setting/', setting, name='setting'),
    path('create/', create_post, name='create_post'),
    path('like/<int:post_id>/', like_post, name='like_post'),
    path('save/<int:post_id>/', save_post, name='save_post'),
        path('unsave_post/<int:post_id>/', unsave_post, name='unsave_post'),

    path('saved/', saved_posts, name='saved_posts'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('help/', views.help, name='help'),
]
