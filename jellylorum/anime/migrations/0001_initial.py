# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Anime'
        db.create_table('anime_anime', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
        ))
        db.send_create_signal('anime', ['Anime'])

        # Adding model 'AP'
        db.create_table('anime_ap', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('anime', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anime.Anime'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('episodeCount', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('startDate', self.gf('django.db.models.fields.DateField')()),
            ('endDate', self.gf('django.db.models.fields.DateField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('anime', ['AP'])

        # Adding model 'AniDB'
        db.create_table('anime_anidb', (
            ('anime', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anime.Anime'])),
            ('id', self.gf('django.db.models.fields.PositiveIntegerField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('episodeCount', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('startDate', self.gf('django.db.models.fields.DateField')()),
            ('endDate', self.gf('django.db.models.fields.DateField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('anime', ['AniDB'])

        # Adding model 'ANN'
        db.create_table('anime_ann', (
            ('anime', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anime.Anime'])),
            ('id', self.gf('django.db.models.fields.PositiveIntegerField')(primary_key=True)),
            ('episodeCount', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('startDate', self.gf('django.db.models.fields.DateField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('anime', ['ANN'])


    def backwards(self, orm):
        
        # Deleting model 'Anime'
        db.delete_table('anime_anime')

        # Deleting model 'AP'
        db.delete_table('anime_ap')

        # Deleting model 'AniDB'
        db.delete_table('anime_anidb')

        # Deleting model 'ANN'
        db.delete_table('anime_ann')


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
            'endDate': ('django.db.models.fields.DateField', [], {}),
            'episodeCount': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'startDate': ('django.db.models.fields.DateField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['anime']
