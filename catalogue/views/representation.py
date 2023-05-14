from django.shortcuts import render
from django.http import Http404

from catalogue.models import Representation


# Create your views here.
def index(request):
    representations = Representation.objects.all()
    title = 'Liste des representations'

    return render(request, 'representation/index.html', {
        'representations': representations,
        'title': title
    })


def show(request, representation_id):
    try:
        representation = Representation.objects.get(id=representation_id)
    except Representation.DoesNotExist:
        raise Http404('representation inexistant')

    title = "Fiche d'un representation"

    return render(request, 'representation/show.html', {
        'representation': representation,
        'title': title
    })
