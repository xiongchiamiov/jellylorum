from anime.models import *

from django.core.management.base import BaseCommand
from lxml import etree

class Command(BaseCommand):
	def handle(self, *args, **options):
		with open('dumps/anime-titles.xml') as f:
			xml = f.read()
		doc = etree.fromstring(xml)
		
		for i, anime in enumerate(doc.getchildren()):
			# Quit early for development purposes.
			if i == 4:
				break
			a = Anime()
			a.save()
			AniDB(anime = a, id = int(anime.get('aid'))).save()
			print anime.get('aid')
			a.anidb.update()
			if a.linkAP():
				a.ap.update()

