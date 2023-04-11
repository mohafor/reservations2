from django.shortcuts import render
from django.http import Http404

from catalogue.models import Show


# Create your views here.
def index(request):
	shows = Show.objects.all()
	title = 'Liste des spectacles'
	
	return render(request, 'shouw/index.html', {
		'shows':shows,
		'title':title
	})


def show(request, shouw_id):
	try:
		shouw = Show.objects.get(id=shouw_id)
	except Show.DoesNotExist:
		raise Http404('Spectacle inexistant')
		
	title = "Fiche d'un spectacle"
	
	return render(request, 'shouw/show.html', {
		'shouw':shouw,
		'title':title 
	})
