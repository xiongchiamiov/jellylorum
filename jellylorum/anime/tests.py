# -*- coding: utf-8 -*-
from anime.models import *

from django.test import TestCase

class APTest(TestCase):
	@classmethod
	def setUpClass(cls):
		anime = Anime()
		anime.save()
		
		cls.knt = AP()
		cls.knt.slug = 'kimi-ni-todoke'
		cls.knt.anime = anime
		cls.knt.update()
		
		cls.maxDiff = None

	def test_correct_title(self):
		self.assertEqual('Kimi ni Todoke', self.knt.title)
	
	def test_correct_type(self):
		self.assertEqual('TV', self.knt.type)
	
	def test_correct_number_of_episodes(self):
		self.assertEqual(25, self.knt.episodeCount)

	def test_correct_year_started(self):
		self.assertEqual(2009, self.knt.startDate.year)

	def test_correct_year_ended(self):
		self.assertEqual(2010, self.knt.endDate.year)
	
	def test_correct_description(self):
		self.assertEqual(u"Sawako Kuronuma is just like any other high school girl who wants to make friends and be useful. The only problem is she bears a worrying resemblance to Sadako from 'The Ring!' Because of her reputation, people are not only terrified of her, but small dogs even bark in fear at her presence; in fact, the only person in school who will talk to her is the lively class hottie, Kazehaya. As the pair spends more time together, Kazehaya slowly begins to bring Sawako out of her shell and soon their feelings for each other develop further. Though with her crippling insecurities, lack of social skills, and a series of cruel rumors and misunderstandings, it seems that Sawako's dream of a normal life won’t be quite so easy to obtain.",
		                 self.knt.description)

class AniDBTest(TestCase):
	@classmethod
	def setUpClass(cls):
		anime = Anime()
		anime.save()
		anime2 = Anime()
		anime2.save()
		
		cls.tt = AniDB()
		cls.tt.id = 9434
		cls.tt.anime = anime
		cls.tt.update()

		cls.ktm = AniDB()
		cls.ktm.id = 6468
		cls.ktm.anime = anime2
		cls.ktm.update()
		
		cls.maxDiff = None
	
	def test_correct_title(self):
		self.assertEqual('Gokicha!! Cockroach Girls', self.tt.title)
		self.assertEqual('Kaguya-hime: Taketori Monogatari', self.ktm.title)

	def test_correct_type(self):
		self.assertEqual('Web', self.tt.type)
		self.assertEqual('OVA', self.ktm.type)

	def test_correct_number_of_episodes(self):
		self.assertEqual(2, self.tt.episodeCount)
		self.assertEqual(1, self.ktm.episodeCount)

	def test_correct_year_started(self):
		self.assertEqual('2012-09-14', self.tt.startDate.strftime('%Y-%m-%d'))
		self.assertEqual(1987, self.ktm.startDate.year)

	def test_correct_year_ended(self):
		self.assertEqual(None, self.tt.endDate)
		self.assertEqual(1987, self.ktm.endDate.year)
	
	def test_correct_website(self):
		self.assertEqual('http://ch.nicovideo.jp/channel/ch60379', self.tt.website)
		self.assertEqual(None, self.ktm.website)

	def test_correct_description(self):
		self.assertEqual('A heartwarming story about a cockroach girl who tries to be liked by humans while dodging the insecticide.',
		                 self.tt.description)
		self.assertEqual('An erotic version of the classical Japanese folktale "The Tale of the Bamboo Cutter", produced by Tokyo Studio.',
		                 self.ktm.description)

class ANNTest(TestCase):
	@classmethod
	def setUpClass(cls):
		anime = Anime()
		anime.save()
		
		cls.knt = ANN()
		cls.knt.id = 10625
		cls.knt.anime = anime
		cls.knt.update()
		
		cls.maxDiff = None
	
	def test_correct_number_of_episodes(self):
		self.assertEqual(25, self.knt.episodeCount)

	def test_correct_year_started(self):
		self.assertEqual('2009-10-06', self.knt.startDate.strftime('%Y-%m-%d'))

	def test_correct_year_ended(self):
		self.assertEqual('2010-03-30', self.knt.endDate.strftime('%Y-%m-%d'))
	
	def test_correct_description(self):
		self.assertEqual(u"Sawako Kuronuma's one wish in life is to make friends. That's a difficult proposition when everyone who meets her cowers in terror, due to her resemblance to Sadako (after whom they nickname her) from the Japanese horror movie series The Ring . Shunned by her classmates, her life starts to change after she befriends her classmate, Shōta Kazehaya, a popular, easygoing and 100% refreshing guy who is nice with everyone, even with her.",
		                self.knt.description)

