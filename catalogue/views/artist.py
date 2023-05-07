from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

from catalogue.models import Artist
from catalogue.forms import ArtistForm, ArtistDeleteForm


# Create your views here.
def index(request):
    artists = Artist.objects.all()

    title = 'Liste des artistes'

    return render(request, 'artist/index.html', {
        'artists': artists,
        'title': title
    })


def show(request, artist_id):
    try:
        artist = Artist.objects.get(id=artist_id)
    except Artist.DoesNotExist:
        raise Http404('Artist inexistant')

    title = 'Fiche d\'un artiste'

    return render(request, 'artist/show.html', {
        'artist': artist,
        'title': title
    })

def create(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue:artist_index')
    else:
        form = ArtistForm()

    title = 'Création d\'un artiste'

    return render(request, 'artist/create.html', {
        'form': form,
        'title': title
    })

def edit(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)

    if request.method == 'POST':
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('catalogue:artist_show', artist_id=artist.id)
    else:
        form = ArtistForm(instance=artist)

    title = 'Modifier un artiste'

    return render(request, 'artist/edit.html', {
        'artist': artist,
        'form': form,
        'title': title
    })
def delete(request, artist_id):
    try:
        artist = Artist.objects.get(id=artist_id)
    except Artist.DoesNotExist:
        raise Http404('Artist inexistant')

    if request.method == 'POST':
        form = ArtistDeleteForm(request.POST, instance=artist)
        if form.is_valid():
            artist.delete()
            return redirect('catalogue:artist_index')
    else:
        form = ArtistDeleteForm(instance=artist)

    title = 'Supprimer un artiste'

    return render(request, 'artist/delete.html', {
        'artist': artist,
        'form': form,
        'title': title
    })