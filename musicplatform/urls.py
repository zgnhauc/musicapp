from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from music import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about),
    path('songs/', views.songs, name='songs'),
    path('songs/<int:song_id>/', views.song_detail, name='song_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('history/', views.history, name='history'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
