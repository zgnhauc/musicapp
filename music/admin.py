from django.contrib import admin
from .models import LogMessage, Song, Rating, ListeningHistory


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'album', 'release_year')
    search_fields = ('title', 'artist', 'album')
    list_filter = ('release_year',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('song', 'rating', 'comment', 'created_at')
    search_fields = ('song__title', 'comment')
    list_filter = ('rating', 'created_at')


@admin.register(ListeningHistory)
class ListeningHistoryAdmin(admin.ModelAdmin):
    list_display = ('song', 'listened_at')
    search_fields = ('song__title',)
    list_filter = ('listened_at',)


@admin.register(LogMessage)
class LogMessageAdmin(admin.ModelAdmin):
    list_display = ('message', 'created_at')
    search_fields = ('message',)
    list_filter = ('created_at',)
