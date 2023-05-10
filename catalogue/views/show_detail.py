from django.shortcuts import render
from django.http import Http404

from catalogue.models import Show, ArtistType


# Create your views here.
def index(request):
	shows = Show.objects.all()
	title = 'Liste des spectacles'
	
	return render(request, 'show/index.html', {
		'shows':shows,
		'title':title
	})


def show(request, show_id):
	
	try:
		show2 = Show.objects.get(id=show_id)
	except Show.DoesNotExist:
		raise Http404('Spectacle inexistant')
	# Récupérer les artistes du spectacle et les grouper par type
	collaborateurs = {}

	for at in  ArtistType.objects.filter(id=show_id):
		collaborateurs.setdefault(at.type.type, []).append(at.artist)
	
	return render(request, 'show/show.html', {
		'show':show2,
		'collaborateurs': collaborateurs,	
	})
