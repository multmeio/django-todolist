# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TodoList'
        db.create_table(u'todolist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
        ))
        db.send_create_signal('core', ['TodoList'])


    def backwards(self, orm):
        # Deleting model 'TodoList'
        db.delete_table(u'todolist')


    models = {
        'core.todolist': {
            'Meta': {'object_name': 'TodoList', 'db_table': "u'todolist'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['core']