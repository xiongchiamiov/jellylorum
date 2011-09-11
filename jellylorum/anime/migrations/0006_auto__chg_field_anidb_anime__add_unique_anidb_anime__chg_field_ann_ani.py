# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'AniDB.anime'
        db.alter_column('anime_anidb', 'anime_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anime.Anime'], unique=True))

        # Adding unique constraint on 'AniDB', fields ['anime']
        db.create_unique('anime_anidb', ['anime_id'])

        # Changing field 'ANN.anime'
        db.alter_column('anime_ann', 'anime_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anime.Anime'], unique=True))

        # Adding unique constraint on 'ANN', fields ['anime']
        db.create_unique('anime_ann', ['anime_id'])

        # Changing field 'AP.anime'
        db.alter_column('anime_ap', 'anime_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['anime.Anime'], unique=True))

        # Adding unique constraint on 'AP', fields ['anime']
        db.create_unique('anime_ap', ['anime_id'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'AP', fields ['anime']
        db.delete_unique('anime_ap', ['anime_id'])

        # Removing unique constraint on 'ANN', fields ['anime']
        db.delete_unique('anime_ann', ['anime_id'])

        # Removing unique constraint on 'AniDB', fields ['anime']
        db.delete_unique('anime_anidb', ['anime_id'])

        # Changing field 'AniDB.anime'
        db.alter_column('anime_anidb', 'anime_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anime.Anime']))

        # Changing field 'ANN.anime'
        db.alter_column('anime_ann', 'anime_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anime.Anime']))

        # Changing field 'AP.anime'
        db.alter_column('anime_ap', 'anime_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anime.Anime']))


    models = {
        'anime.anidb': {
            'Meta': {'object_name': 'AniDB'},
            'anime': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anime.Anime']", 'unique': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'endDate': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'episodeCount': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'startDate': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '30'})
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
            'id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'startDate': ('django.db.models.fields.DateField', [], {})
        },
        'anime.ap': {
            'Meta': {'object_name': 'AP'},
            'anime': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['anime.Anime']", 'unique': 'True'}),
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
