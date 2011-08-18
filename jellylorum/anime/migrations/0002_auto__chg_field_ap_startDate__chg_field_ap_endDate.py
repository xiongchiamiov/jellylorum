# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'AP.startDate'
        db.alter_column('anime_ap', 'startDate', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'AP.endDate'
        db.alter_column('anime_ap', 'endDate', self.gf('django.db.models.fields.DateField')(null=True))


    def backwards(self, orm):
        
        # Changing field 'AP.startDate'
        db.alter_column('anime_ap', 'startDate', self.gf('django.db.models.fields.DateField')(default=None))

        # Changing field 'AP.endDate'
        db.alter_column('anime_ap', 'endDate', self.gf('django.db.models.fields.DateField')(default=None))


    models = {
        'anime.anidb': {
            'Meta': {'object_name': 'AniDB'},
            'anime': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anime.Anime']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'endDate': ('django.db.models.fields.DateField', [], {}),
            'episodeCount': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'startDate': ('django.db.models.fields.DateField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'anime.anime': {
            'Meta': {'object_name': 'Anime'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'anime.ann': {
            'Meta': {'object_name': 'ANN'},
            'anime': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anime.Anime']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'episodeCount': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'startDate': ('django.db.models.fields.DateField', [], {})
        },
        'anime.ap': {
            'Meta': {'object_name': 'AP'},
            'anime': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anime.Anime']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'endDate': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'episodeCount': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'startDate': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['anime']
