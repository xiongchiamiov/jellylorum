from anime.models import *

from django.core.management.base import BaseCommand
from lxml import etree
from time import sleep

class Command(BaseCommand):
	def handle(self, *args, **options):
		with open('dumps/anime-titles.xml') as f:
			xml = f.read()
		doc = etree.fromstring(xml)
		
		linked = 0
		for i, anime in enumerate(doc.getchildren()):
			# Quit early for development purposes.
			if i == 100:
				break
			a = Anime()
			a.save()
			AniDB(anime = a, id = int(anime.get('aid'))).save()
			print anime.get('aid')
			a.anidb.update()
			if a.linkAP():
				a.ap.update()
				linked += 1
			sleep(5)
		print "%s of %s linked successfully." % (linked, i)

