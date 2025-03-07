from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from posts.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('accounts/', include('accounts.urls')),
    # path('accounts/login/', include('django.contrib.auth.urls')),
    path('posts/', include('posts.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)