from django.shortcuts import render
from django.http import Http404

from catalogue.models import Locality


# Create your views here.
def index(request):
    localities = Locality.objects.all()

    title = 'Liste des localities'

    return render(request, 'locality/index.html', {
    'localities': localities,
    'title': title
})


def show(request, locality_id):
    try:
        locality = Locality.objects.get(id=locality_id)
    except Locality.DoesNotExist:
        raise Http404('Locality inexistant')

    title = 'Fiche d\'un locality'

    return render(request, 'locality/show.html', {
        'locality': locality,
        'title': title
    })
