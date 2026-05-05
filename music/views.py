from django.shortcuts import render, get_object_or_404
from .models import LogMessage, Song, Rating

def home(request):
    logs = LogMessage.objects.all()
    return render(request, 'musicplatform/home.html', {'logs': logs})

def about(request):
    return render(request, 'musicplatform/about.html')

def songs(request):
    songs = Song.objects.all()
    return render(request, 'music/songs.html', {'songs': songs})

def song_detail(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    ratings = Rating.objects.filter(song=song)

    if request.method == 'POST':
        rating_value = request.POST.get('rating')
        comment = request.POST.get('comment', '')
        Rating.objects.create(song=song, rating=rating_value, comment=comment)
        ratings = Rating.objects.filter(song=song)

    return render(request, 'music/song_detail.html', {'song': song, 'ratings': ratings})