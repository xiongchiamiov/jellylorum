# -*- coding: utf-8 -*-
from anime.models import *

from django.test import TestCase

class APTest(TestCase):
	@classmethod
	def setUpClass(cls):
		cls.knt = AP()
		cls.knt.slug = 'kimi-ni-todoke'
		cls.knt.update()

	def test_correct_type(self):
		self.assertEqual('TV', self.knt.type)
	
	def test_correct_number_of_episodes(self):
		self.assertEqual(25, self.knt.episodeCount)

	def test_correct_year_started(self):
		self.assertEqual(2009, self.knt.startDate.year)

	def test_correct_year_ended(self):
		self.assertEqual(2010, self.knt.endDate.year)
	
	def test_correct_description(self):
		self.assertEqual(u"Sawako Kuronuma is just like any other high school girl who wants to make friends and be useful. The only problem is she bears a worrying resemblance to Sadako from 'The Ring!' Because of her reputation, people are not only terrified of her, but small dogs even bark in fear at her presence; in fact, the only person in school who will talk to her is the lively class hottie, Kazehara. As the pair spends more time together, Kazehara slowly begins to bring Sawako out of her shell and soon their feelings for each other develop further. Though with her crippling insecurities, lack of social skills, and a series of cruel rumors and misunderstandings, it seems that Sawako's dream of a normal life won’t be quite so easy to obtain.",
		                 self.knt.description)

class AniDBTest(TestCase):
	@classmethod
	def setUpClass(cls):
		cls.working = AniDB()
		cls.working.id = 8364
		cls.working.update()

		cls.ktm = AniDB()
		cls.ktm.id = 6468
		cls.ktm.update()

	def test_correct_type(self):
		self.assertEqual('TV Series', self.working.type)
		self.assertEqual('OVA', self.ktm.type)

	def test_correct_number_of_episodes(self):
		# Don't ask me why Working has one episode when the web ui shows an unknown number.
		# That's what's in the XML response, though, so that's what I should expect here.
		self.assertEqual(1, self.working.episodeCount)
		self.assertEqual(1, self.ktm.episodeCount)

	def test_correct_year_started(self):
		self.assertEqual('2011-09-03', self.working.startDate.strftime('%Y-%m-%d'))
		self.assertEqual(1987, self.ktm.startDate.year)

	def test_correct_year_ended(self):
		self.assertEqual(None, self.working.endDate)
		self.assertEqual(1987, self.ktm.endDate.year)

	def test_correct_description(self):
		self.assertEqual('Note: The first episode received a preview airing on September 3. The regular television airing started on October, 2011.',
		                 self.working.description)
		self.assertEqual('An erotic version of the classical Japanese folktale "The Tale of the Bamboo Cutter", produced by Tokyo Studio.',
		                 self.ktm.description)

