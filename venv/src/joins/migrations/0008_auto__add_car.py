# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Car'
        db.create_table(u'joins_car', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Sharer', to=orm['joins.Join'])),
            ('emailall', self.gf('django.db.models.fields.related.ForeignKey')(related_name='emailall', to=orm['joins.Join'])),
        ))
        db.send_create_signal(u'joins', ['Car'])

        # Adding M2M table for field friends on 'Car'
        m2m_table_name = db.shorten_name(u'joins_car_friends')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('car', models.ForeignKey(orm[u'joins.car'], null=False)),
            ('join', models.ForeignKey(orm[u'joins.join'], null=False))
        ))
        db.create_unique(m2m_table_name, ['car_id', 'join_id'])


    def backwards(self, orm):
        # Deleting model 'Car'
        db.delete_table(u'joins_car')

        # Removing M2M table for field friends on 'Car'
        db.delete_table(db.shorten_name(u'joins_car_friends'))


    models = {
        u'joins.car': {
            'Meta': {'object_name': 'Car'},
            'email': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Sharer'", 'to': u"orm['joins.Join']"}),
            'emailall': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'emailall'", 'to': u"orm['joins.Join']"}),
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'Friend'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['joins.Join']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'joins.join': {
            'Meta': {'unique_together': "(('email', 'ref_id'),)", 'object_name': 'Join'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'default': "'ABC'", 'max_length': '120'}),
            'ref_id': ('django.db.models.fields.CharField', [], {'default': "'ABC'", 'unique': 'True', 'max_length': '120'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['joins']