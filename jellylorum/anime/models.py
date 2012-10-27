import sys
from datetime import datetime
from decimal import Decimal
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
	studio = models.CharField(max_length=30)
	startDate = models.DateField(blank=True, null=True, default=None)
	endDate = models.DateField(blank=True, null=True, default=None)
	rating = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True, default=None)
	description = models.TextField()

	def update(self):
		q = PyQuery(url='http://www.anime-planet.com/anime/'+self.slug)
		
		self.title = q('#anime .theme').text()

		html = q('.tabPanelLeft .type').text()
		(type, episodeCount) = match(r'^(\w+) \((\d+\+?)', html).groups()
		self.type = type
		self.episodeCount = int(episodeCount)

		self.studio = q('.tabPanelLeft .studio').text()

		self.description = q('.entryContent .synopsis p').text()

		html = q('.tabPanelLeft .year').text()
		matches = match(r'(\d+|\?) - (\d+|\?)', html)
		if matches:
			(startDate, endDate) = matches.groups()
		else:
			# Movies, OVAs, and some TV series start and end in the same year.
			startDate = endDate = match(r'(\d+|\?)', html).groups()[0]
		self.startDate = datetime.strptime(startDate, '%Y') if startDate != '?' else None
		self.endDate = datetime.strptime(endDate, '%Y') if endDate != '?' else None

		html = q('.tabPanelLeft .avgRating span').text()
		matches = match(r'^([\d.]+) out of', html)
		if matches:
			self.rating = Decimal(matches.groups()[0])
		# Sometimes there aren't enough ratings yet to provide an average.
		else:
			self.rating = None

		self.save()

class AniDB(models.Model):
	anime = models.OneToOneField(Anime)

	id = models.PositiveIntegerField(primary_key=True)
	title = models.CharField(max_length=128)
	type = models.CharField(max_length=30, choices=TYPE_CHOICES)
	rawAverageRating = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True, default=None)
	weightedAverageRating = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True, default=None)
	reviewRating = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True, default=None)
	episodeCount = models.PositiveSmallIntegerField()
	startDate = models.DateField(blank=True, null=True, default=None)
	endDate = models.DateField(blank=True, null=True, default=None)
	website = models.CharField(max_length=128, blank=True, null=True, default=None)
	description = models.TextField()
	categories = models.CharField(max_length=1024, blank=True, null=True, default=None)

	def update(self):
		url = 'http://api.anidb.net:9001/httpapi?request=anime&client=jellylorum&clientver=1&protover=1&aid=%s' % self.id
		response = urlopen(url)
		buffer = StringIO(response.read())
		file = GzipFile(fileobj=buffer)
		xml = file.read()

		doc = etree.fromstring(xml)
		
		for title in doc.find('titles'):
			if title.get('type') == 'main':
				self.title = title.text
				break
		
		# The 'temporary' and 'permanent' fields now mean different things than
		# their names imply.
		# http://anidb.net/perl-bin/animedb.pl?show=cmt&id=45058
		rawAverageRating = doc.find('ratings').find('temporary')
		if rawAverageRating is not None:
			self.rawAverageRating = Decimal(rawAverageRating.text)
		else:
			self.rawAverageRating = None
		weightedAverageRating = doc.find('ratings').find('permanent')
		if weightedAverageRating is not None:
			self.weightedAverageRating = Decimal(weightedAverageRating.text)
		else:
			self.weightedAverageRating = None
		reviewRating = doc.find('ratings').find('review')
		if reviewRating is not None:
			self.reviewRating = Decimal(reviewRating.text)
		else:
			self.reviewRating = None

		self.type = doc.find('type').text
		self.episodeCount = int(doc.find('episodecount').text)
		self.description = doc.find('description').text
		
		website = doc.find('url')
		# lxml.etree.Element has a broken __nonzero__ method, so bool(website)
		# is false even when it exists and has text.
		if website is not None:
			self.website = website.text

		startDate = doc.find('startdate')
		endDate = doc.find('enddate')
		self.startDate = self.parseDate(startDate)
		self.endDate = self.parseDate(endDate)
		
		# My inner DBA is cringing as I write this, and should yours.  But hold
		# on for a minute while I explain.
		# All of the nice Django extensions for doing "tags" use many-to-many
		# relationships, at their heart.  Go ahead, look through the source of
		# django-tagging and django-taggit.  Performing M2Ms when you don't
		# have to is a Bad Thing.
		# And I really don't have to.  Serializing data like this means we
		# can't query on it - but that's ok.  It means it's difficult to
		# present it in any other way than a single string - but that's ok.
		# All this project is ever intended to do is display information on a
		# particular show - *not* to provide ways to browse for new shows;
		# that's what the source sites are for.  Implementing categories like
		# this helps keep the project in scope and reduces complexity.
		categories = []
		for category in doc.find('categories'):
			categories.append(category.find('name').text)
		# The API doesn't seem to return categories in any particular order.
		# Perhaps we should sort by weight, then alphabetical?
		categories.sort()
		self.categories = ', '.join(categories)
		
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

