# -*- coding: utf-8 -*-
from haystack import indexes

from anime.models import *

class AnimeIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	
	def get_model(self):
		return Anime

