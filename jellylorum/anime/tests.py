# -*- coding: utf-8 -*-
from anime.models import *

from decimal import Decimal
from django.test import TestCase

class AnimeTest(TestCase):
	@classmethod
	def setUpClass(cls):
		cls.gcg = Anime()
		cls.gcg.save()
		cls.fma = Anime()
		cls.fma.save()
		
		anidb = AniDB()
		anidb.id = 9434
		anidb.anime = cls.gcg
		anidb.update()
		
		anidb2 = AniDB()
		anidb2.id = 6107
		anidb2.anime = cls.fma
		anidb2.update()
	
	def test_ap_linking(self):
		self.gcg.linkAP()
		self.assertEqual('gokicha-cockroach-girls', self.gcg.ap.slug)
		
		self.fma.linkAP()
		# The second parameter to assertRaises needs to strictly be a callable -
		# if we don't wrap the variable access in a lambda, it doesn't catch the
		# exception.
		self.assertRaises(AP.DoesNotExist, lambda: self.fma.ap)

class APTest(TestCase):
	@classmethod
	def setUpClass(cls):
		anime = Anime()
		anime.save()
		anime2 = Anime()
		anime2.save()
		anime3 = Anime()
		anime3.save()
		
		cls.knt = AP()
		cls.knt.slug = 'kimi-ni-todoke'
		cls.knt.anime = anime
		cls.knt.update()

		cls.ysbl = AP()
		cls.ysbl.slug = 'you-shoumei-bijutsukan-line'
		cls.ysbl.anime = anime2
		cls.ysbl.update()
		
		cls.cots = AP()
		cls.cots.slug = 'crest-of-the-stars-birth'
		cls.cots.anime = anime3
		cls.cots.update()
		
		cls.maxDiff = None

	def test_correct_title(self):
		self.assertEqual('Kimi ni Todoke', self.knt.title)
		self.assertEqual('You Shoumei Bijutsukan Line', self.ysbl.title)
	
	def test_correct_type(self):
		self.assertEqual('TV', self.knt.type)
		self.assertEqual('OVA', self.ysbl.type)
		self.assertEqual('TV Special', self.cots.type)
	
	def test_correct_number_of_episodes(self):
		self.assertEqual(25, self.knt.episodeCount)
		self.assertEqual(1, self.ysbl.episodeCount)
	
	def test_correct_studio(self):
		self.assertEqual('Production I.G', self.knt.studio)
		self.assertEqual(None, self.ysbl.studio)

	def test_correct_year_started(self):
		self.assertEqual(2009, self.knt.startDate.year)
		self.assertEqual(2006, self.ysbl.startDate.year)

	def test_correct_year_ended(self):
		self.assertEqual(2010, self.knt.endDate.year)
		self.assertEqual(2006, self.ysbl.endDate.year)
	
	def test_correct_rating(self):
		self.assertAlmostEqual(4.369, float(self.knt.rating),
		                       delta=0.35)
		# TODO: Find another show with no rating.
		self.assertAlmostEqual(1.378, float(self.ysbl.rating),
		                       delta=0.35)
	
	def test_correct_rank(self):
		self.assertAlmostEqual(143, self.knt.rank, delta=20)
		# TODO: Find another show with no rating (and thus no rank).
		self.assertAlmostEqual(4810, self.ysbl.rank, delta=20)
	
	def test_correct_description(self):
		self.assertEqual(u"Sawako Kuronuma is just like any other high school girl who wants to make friends and be useful. The only problem is she bears a worrying resemblance to Sadako from 'The Ring!' Because of her reputation, people are not only terrified of her, but small dogs even bark in fear at her presence; in fact, the only person in school who will talk to her is the lively class hottie, Kazehaya. As the pair spends more time together, Kazehaya slowly begins to bring Sawako out of her shell and soon their feelings for each other develop further. Though with her crippling insecurities, lack of social skills, and a series of cruel rumors and misunderstandings, it seems that Sawako's dream of a normal life won’t be quite so easy to obtain.",
		                 self.knt.description)
		self.assertEqual(u"No synopsis yet - check back soon!", self.ysbl.description)
	
	def test_correct_tags(self):
		self.assertEqual('Comedy, Drama, Romance, Shoujo, School Life',
		                 self.knt.tags)
		self.assertEqual(None, self.ysbl.tags)

class AniDBTest(TestCase):
	@classmethod
	def setUpClass(cls):
		anime = Anime()
		anime.save()
		anime2 = Anime()
		anime2.save()
		
		cls.gcg = AniDB()
		cls.gcg.id = 9434
		cls.gcg.anime = anime
		cls.gcg.update()

		cls.ktm = AniDB()
		cls.ktm.id = 6468
		cls.ktm.anime = anime2
		cls.ktm.update()
		
		cls.maxDiff = None
	
	def test_correct_title(self):
		self.assertEqual('Gokicha!! Cockroach Girls', self.gcg.title)
		self.assertEqual('Kaguya-hime: Taketori Monogatari', self.ktm.title)

	def test_correct_type(self):
		self.assertEqual('Web', self.gcg.type)
		self.assertEqual('OVA', self.ktm.type)
	
	def test_correct_votes(self):
		self.assertAlmostEqual(5.72, float(self.gcg.rawAverageRating),
		                       delta=0.35)
		self.assertAlmostEqual(2.79, float(self.gcg.weightedAverageRating),
		                       delta=0.35)
		self.assertEqual(None, self.gcg.reviewRating)
		
		self.assertAlmostEqual(4.45, float(self.ktm.rawAverageRating),
		                       delta=0.35)
		self.assertAlmostEqual(4.49, float(self.ktm.weightedAverageRating),
		                       delta=0.35)
		self.assertEqual(None, self.ktm.reviewRating)

	def test_correct_number_of_episodes(self):
		self.assertEqual(2, self.gcg.episodeCount)
		self.assertEqual(1, self.ktm.episodeCount)

	def test_correct_year_started(self):
		self.assertEqual('2012-09-14', self.gcg.startDate.strftime('%Y-%m-%d'))
		self.assertEqual(1987, self.ktm.startDate.year)

	def test_correct_year_ended(self):
		self.assertEqual(None, self.gcg.endDate)
		self.assertEqual(1987, self.ktm.endDate.year)
	
	def test_correct_website(self):
		self.assertEqual('http://ch.nicovideo.jp/channel/ch60379', self.gcg.website)
		self.assertEqual(None, self.ktm.website)

	def test_correct_description(self):
		self.assertEqual('A heartwarming story about a cockroach girl who tries to be liked by humans while dodging the insecticide.',
		                 self.gcg.description)
		self.assertEqual('An erotic version of the classical Japanese folktale The Tale of the Bamboo Cutter, produced by Tokyo Studio.',
		                 self.ktm.description)
	
	def test_correct_categories(self):
		self.assertEqual('4-koma, Anthropomorphism, Comedy, Cooking, Daily Life, Hokkaido, Manga, Present, Romance, Slapstick',
		                 self.gcg.categories)
		self.assertEqual('18 Restricted, Historical, Japan, Nudity, Past, Sex, Virgin',
		                 self.ktm.categories)
	
	def test_correct_tags(self):
		self.assertEqual('animal perspective, female protagonist, for mobile phone, moe',
		                 self.gcg.tags)
		self.assertEqual('', self.ktm.tags)

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
	
	def test_correct_genres(self):
		self.assertEqual(u'comedy, romance, slice of life', self.knt.genres)
	
	def test_correct_themes(self):
		self.assertEqual(u'school', self.knt.themes)
	
	def test_correct_objectionable_content(self):
		self.assertEqual(u'Mild', self.knt.objectionableContent)
	
	def test_correct_description(self):
		self.assertEqual(u"Sawako Kuronuma's one wish in life is to make friends. That's a difficult proposition when everyone who meets her cowers in terror, due to her resemblance to Sadako (after whom they nickname her) from the Japanese horror movie series The Ring . Shunned by her classmates, her life starts to change after she befriends her classmate, Shōta Kazehaya, a popular, easygoing and 100% refreshing guy who is nice with everyone, even with her.",
		                self.knt.description)

