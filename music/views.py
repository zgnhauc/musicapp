from django.shortcuts import render
from .models import LogMessage

def home(request):
    # This fetches all logs from the database to show on your home page
    logs = LogMessage.objects.all()
    return render(request, 'musicplatform/home.html', {'logs': logs})