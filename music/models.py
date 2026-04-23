from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=200, blank=True)
    release_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


class Rating(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    rating = models.IntegerField()  # 1–5 stars
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.song.title} - {self.rating} stars"


class ListeningHistory(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    listened_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Listened: {self.song.title}"
    
class LogMessage(models.Model):
    # This stores the text for your log entries
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
