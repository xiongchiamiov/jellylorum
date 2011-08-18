from datetime import datetime
from django.db import models
from pyquery import PyQuery
from re import match

class Anime(models.Model):
	slug = models.SlugField()

TYPE_CHOICES = (
	('TV', 'TV'),
	('OVA', 'OVA'),
	('Movie', 'Movie'),
)

class AP(models.Model):
	anime = models.ForeignKey(Anime)

	slug = models.SlugField(unique=True)
	type = models.CharField(max_length=30, choices=TYPE_CHOICES)
	episodeCount = models.PositiveSmallIntegerField()
	startDate = models.DateField(blank=True, null=True, default=None)
	endDate = models.DateField(blank=True, null=True, default=None)
	description = models.TextField()

	def update(self):
		q = PyQuery(url='http://www.anime-planet.com/anime/'+self.slug)

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
	anime = models.ForeignKey(Anime)

	id = models.PositiveIntegerField(primary_key=True)
	type = models.CharField(max_length=30, choices=TYPE_CHOICES)
	episodeCount = models.PositiveSmallIntegerField()
	startDate = models.DateField()
	endDate = models.DateField()
	description = models.TextField()

class ANN(models.Model):
	anime = models.ForeignKey(Anime)

	id = models.PositiveIntegerField(primary_key=True)
	episodeCount = models.PositiveSmallIntegerField()
	startDate = models.DateField()
	description = models.TextField()

