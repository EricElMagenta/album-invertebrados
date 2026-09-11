from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def start(request):
    if request.user.is_authenticated: return redirect('album-home')
    return render(request, 'album/start.html')


@login_required
def home(request):
    context = {
        'user' : request.user
    }
    return render(request, 'album/home.html', context)