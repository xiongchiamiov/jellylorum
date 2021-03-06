# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'AP.studio'
        db.alter_column('anime_ap', 'studio', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))


    def backwards(self, orm):
        
        # Changing field 'AP.studio'
        db.alter_column('anime_ap', 'studio', self.gf('django.db.models.fields.CharField')(default=None, max_length=30))


    models = {
        'anime.anidb': {
            'Meta': {'object_name': 'AniDB'},
            'anime': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anime.Anime']", 'unique': 'True'}),
            'categories': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'endDate': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'episodeCount': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'rawAverageRating': ('django.db.models.fields.DecimalField', [], {'default': 'None', 'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'reviewRating': ('django.db.models.fields.DecimalField', [], {'default': 'None', 'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'startDate': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'website': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'weightedAverageRating': ('django.db.models.fields.DecimalField', [], {'default': 'None', 'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'})
        },
        'anime.anime': {
            'Meta': {'object_name': 'Anime'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'anime.ann': {
            'Meta': {'object_name': 'ANN'},
            'anime': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anime.Anime']", 'unique': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'endDate': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'episodeCount': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'genres': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'objectionableContent': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'startDate': ('django.db.models.fields.DateField', [], {}),
            'themes': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '1024', 'null': 'True', 'blank': 'True'})
        },
        'anime.ap': {
            'Meta': {'object_name': 'AP'},
            'anime': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anime.Anime']", 'unique': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'endDate': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'episodeCount': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rank': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.DecimalField', [], {'default': 'None', 'null': 'True', 'max_digits': '4', 'decimal_places': '3', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'startDate': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'studio': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['anime']
