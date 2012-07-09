import sys
from datetime import datetime
from django.db import models
from gzip import GzipFile
from lxml import etree
from pyquery import PyQuery
from re import match
from StringIO import StringIO
from urllib2 import urlopen

class Anime(models.Model):
	slug = models.SlugField()

TYPE_CHOICES = (
	('TV', 'TV'),
	('OVA', 'OVA'),
	('Movie', 'Movie'),
)

class AP(models.Model):
	anime = models.OneToOneField(Anime)

	slug = models.SlugField(unique=True)
	title = models.CharField(max_length=255)
	type = models.CharField(max_length=30, choices=TYPE_CHOICES)
	episodeCount = models.PositiveSmallIntegerField()
	startDate = models.DateField(blank=True, null=True, default=None)
	endDate = models.DateField(blank=True, null=True, default=None)
	description = models.TextField()

	def update(self):
		q = PyQuery(url='http://www.anime-planet.com/anime/'+self.slug)
		
		self.title = q('#anime .theme').text()

		html = q('.tabPanelLeft .type').text()
		(type, episodeCount) = match(r'^(\w+) \((\d+\+?)', html).groups()
		self.type = type
		self.episodeCount = int(episodeCount)

		self.description = q('.entryContent .synopsis p').text()

		html = q('.tabPanelLeft .year').text()
		(startDate, endDate) = match(r'(\d+|\?) - (\d+|\?)', html).groups()
		self.startDate = datetime.strptime(startDate, '%Y') if startDate != '?' else None
		self.endDate = datetime.strptime(endDate, '%Y') if endDate != '?' else None

		self.save()

class AniDB(models.Model):
	anime = models.OneToOneField(Anime)

	id = models.PositiveIntegerField(primary_key=True)
	type = models.CharField(max_length=30, choices=TYPE_CHOICES)
	episodeCount = models.PositiveSmallIntegerField()
	startDate = models.DateField(blank=True, null=True, default=None)
	endDate = models.DateField(blank=True, null=True, default=None)
	description = models.TextField()

	def update(self):
		url = 'http://api.anidb.net:9001/httpapi?request=anime&client=jellylorum&clientver=1&protover=1&aid=%s' % self.id
		response = urlopen(url)
		buffer = StringIO(response.read())
		file = GzipFile(fileobj=buffer)
		xml = file.read()

		doc = etree.fromstring(xml)

		self.type = doc.find('type').text
		self.episodeCount = int(doc.find('episodecount').text)
		self.description = doc.find('description').text

		startDate = doc.find('startdate')
		endDate = doc.find('enddate')
		self.startDate = self.parseDate(startDate)
		self.endDate = self.parseDate(endDate)

		self.save()
	
	@staticmethod
	def parseDate(node):
		if node is None:
			return None

		date = node.text
		try:
			return datetime.strptime(date, '%Y-%m-%d')
		except ValueError:
			return datetime.strptime(date, '%Y')

class ANN(models.Model):
	anime = models.OneToOneField(Anime)

	id = models.PositiveIntegerField(primary_key=True)
	episodeCount = models.PositiveSmallIntegerField()
	startDate = models.DateField()
	endDate = models.DateField(blank=True, null=True, default=None)
	description = models.TextField()

	def update(self):
		q = PyQuery(url='http://www.animenewsnetwork.com/encyclopedia/anime.php?id=%s' % self.id)

		# get all sorts of useful information, and some
		infos = q('.encyc-info-type')

		for info in infos:
			info = q(info).text().strip()
			# This is some hackery necessary because of bad encoding handling and ANN being stupid.
			info = info.encode('latin-1').decode('utf-8')
			if info.startswith('Number of episodes'):
				self.episodeCount = int(match(r'Number of episodes: (\d+)', info).groups()[0])
			elif info.startswith('Vintage'):
				(startDate, endDate) = match(r'Vintage: ([\d-]+) to ([\d-]+)', info).groups()
				self.startDate = datetime.strptime(startDate, '%Y-%m-%d')
				self.endDate = datetime.strptime(endDate, '%Y-%m-%d')
			elif info.startswith('Plot Summary'):
				self.description = match(r'Plot Summary: (.*)', info).groups()[0]

		self.save()

