from anime.models import Anime, AP, AniDB, ANN
from django.shortcuts import render_to_response

def details(request, slug):
	data = {}
	data['anime'] = Anime.objects.get(slug=slug)
	return render_to_response('anime/details.html', data)

