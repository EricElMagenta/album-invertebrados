from django.shortcuts import render, redirect
from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Invertebrate

def start(request):
    if request.user.is_authenticated: return redirect('album-home')
    return render(request, 'album/start.html')


@login_required
def home(request):
    context = {
        'user' : request.user
    }
    return render(request, 'album/home.html', context)


@login_required
def album(request):
    invertebrates_array = []
    user = request.user

    for invertebrate in Invertebrate.objects.all():
        if invertebrate.album.user.username == user.username:
            invertebrates_array.append(invertebrate)

    context = {
        'invertebrates' : invertebrates_array,
        'user' : user
    }
    return render(request, 'album/album.html', context)

@login_required
def invertebrate(request, pk):
    context = {
        'invertebrate': Invertebrate.objects.get(id=pk)
    }
    return render(request, 'album/invertebrate.html', context)