# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MyType'
        db.create_table(u'lda_example_mytype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'lda_example', ['MyType'])

        # Adding model 'MyModel'
        db.create_table(u'lda_example_mymodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'lda_example', ['MyModel'])

        # Adding M2M table for field my_type on 'MyModel'
        m2m_table_name = db.shorten_name(u'lda_example_mymodel_my_type')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('mymodel', models.ForeignKey(orm[u'lda_example.mymodel'], null=False)),
            ('mytype', models.ForeignKey(orm[u'lda_example.mytype'], null=False))
        ))
        db.create_unique(m2m_table_name, ['mymodel_id', 'mytype_id'])

        # Adding model 'MyRelatedModel'
        db.create_table(u'lda_example_myrelatedmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('base_model', self.gf('django.db.models.ForeignKey')(to=orm['lda_example.MyType'])),
        ))
        db.send_create_signal(u'lda_example', ['MyRelatedModel'])


    def backwards(self, orm):
        # Deleting model 'MyType'
        db.delete_table(u'lda_example_mytype')

        # Deleting model 'MyModel'
        db.delete_table(u'lda_example_mymodel')

        # Removing M2M table for field my_type on 'MyModel'
        db.delete_table(db.shorten_name(u'lda_example_mymodel_my_type'))

        # Deleting model 'MyRelatedModel'
        db.delete_table(u'lda_example_myrelatedmodel')


    models = {
        u'lda_example.mymodel': {
            'Meta': {'object_name': 'MyModel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'my_type': ('django.db.models.ManyToManyField', [], {'to': u"orm['lda_example.MyType']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'lda_example.myrelatedmodel': {
            'Meta': {'object_name': 'MyRelatedModel'},
            'base_model': ('django.db.models.ForeignKey', [], {'to': u"orm['lda_example.MyType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'lda_example.mytype': {
            'Meta': {'object_name': 'MyType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['lda_example']