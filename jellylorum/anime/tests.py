from anime.models import *

from django.test import TestCase

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

