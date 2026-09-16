from django.shortcuts import render, redirect
from django.apps import apps
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


@login_required
def album(request):
    invertebrates = apps.get_model('album', 'Invertebrate')
    invertebrates_array = []
    user = request.user

    for invertebrate in invertebrates.objects.all():
        if invertebrate.album.user.username == user.username:
            invertebrates_array.append(invertebrate)

    context = {
        'invertebrates' : invertebrates_array,
        'user' : user
    }
    return render(request, 'album/album.html', context)