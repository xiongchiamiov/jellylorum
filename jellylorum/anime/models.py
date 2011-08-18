from django.db import models
from pyquery import PyQuery
from re import match
from time import strptime

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
	startDate = models.DateField()
	endDate = models.DateField()
	description = models.TextField()

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

