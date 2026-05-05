
from django.contrib import admin
from .models import LogMessage, Song, Rating, ListeningHistory

admin.site.register(LogMessage)
admin.site.register(Song)
admin.site.register(Rating)
admin.site.register(ListeningHistory)