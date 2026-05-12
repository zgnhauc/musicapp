#Ambrose Mcahee
from django.shortcuts import render, get_object_or_404, redirect
from .models import LogMessage, Song, Rating, ListeningHistory
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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
        if 'play' in request.POST:
            ListeningHistory.objects.create(song=song)
        else:
            rating_value = request.POST.get('rating')
            comment = request.POST.get('comment', '')
            Rating.objects.create(song=song, rating=rating_value, comment=comment)
            ratings = Rating.objects.filter(song=song)

    return render(request, 'music/song_detail.html', {'song': song, 'ratings': ratings})

def history(request):
    entries = ListeningHistory.objects.order_by('-listened_at')
    return render(request, 'music/history.html', {'entries': entries})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in!"))
            return redirect('home')
        else:
            messages.success(request, ("There was an error, please try again."))
            return redirect('login')
    else:
        return render(request, 'musicplatform/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out. Thank you for using our app!"))
    return redirect('home')
