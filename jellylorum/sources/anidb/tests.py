"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from models import Anime

class ParsingTest(TestCase):
	def setUp(self):
		fin = open('sources/anidb/cache/foo.xml', 'r')
		self.xml = fin.read()
	def test_parse(self):
		"""
		Tests that 1 + 1 always equals 2.
		"""
		anime = Anime._parse(self.xml)
		self.failUnlessEqual(6468, anime.id)
		
		self.failUnlessEqual('OVA', anime.type)
		self.failUnlessEqual(1, anime.episodeCount)
		self.failUnlessEqual(1987, anime.startDate)
		self.failUnlessEqual(1987, anime.endDate)
		self.failUnlessEqual('An erotic version of the classical Japanese folktale "The Tale of the Bamboo Cutter", produced by Tokyo Studio.', anime.description)
