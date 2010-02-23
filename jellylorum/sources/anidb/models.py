import gzip
from django.db import models
from urllib2 import urlopen
from StringIO import StringIO
from xml.etree import ElementTree

class Anime(models.Model):
	def _update(self):
		'''http://api.anidb.net:9001/httpapi?request=anime&client={str}&clientver={int}&protover=1&aid={int}'''
		u = urlopen('http://api.anidb.net:9001/httpapi?request=anime&client=jellylorum&clientver=1&protover=1&aid=6468')
		line = u.read()
		stream = StringIO(line)
		gzipper = gzip.GzipFile(fileobj=stream)
		self = _parse(gzipper.read())
	#http://api.anidb.net:9001/httpapi?request=anime&client=jellylorum&clientver=0&protover=1&aid=6466
	
	@staticmethod
	def _parse(xml):
		tree = ElementTree.fromstring(xml)
		anime = Anime()
		
		anime.id = int(tree.attrib['id'])
		
		anime.type = tree.find('type').text
		anime.episodeCount = int(tree.find('episodecount').text)
		anime.startDate = int(tree.find('startdate').text)
		anime.endDate = int(tree.find('enddate').text)
		anime.description = tree.find('description').text
		
		return anime
