from django.shortcuts import render, redirect, get_object_or_404
from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Invertebrate, Album
from .forms import InvertebrateForm


def start(request):
    if request.user.is_authenticated: return redirect('album-home')
    return render(request, 'album/start.html')


@login_required
def home(request):
    context = {
        'user' : request.user,
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
        'user' : user,
    }
    return render(request, 'album/album.html', context)


@login_required
def invertebrate(request, pk):
    context = {
        'invertebrate': Invertebrate.objects.get(id=pk)
    }

    return render(request, 'album/invertebrate.html', context)


@login_required
def add_invertebrate(request):
    form = InvertebrateForm(request.POST, request.FILES)
    if request.method == 'POST':
        user_album = request.user.album

        if form.is_valid():
            invertebrate = Invertebrate()
            invertebrate.name = form.cleaned_data['name']
            invertebrate.scientific_name = form.cleaned_data['scientific_name']
            invertebrate.taxon_class = form.cleaned_data['taxon_class']
            invertebrate.taxon_order = form.cleaned_data['taxon_order']
            invertebrate.facts = form.cleaned_data['facts']
            invertebrate.image = form.cleaned_data['image']

            invertebrate.album = user_album

            invertebrate.save()
            return redirect('album')

    return render(request, 'album/add_invertebrate.html', {'form': form})


@login_required
def delete_invertebrate(request, pk):
    if request.method == 'POST':
        invertebrate = get_object_or_404(Invertebrate, pk=pk)
        invertebrate.delete()

    return redirect('album')