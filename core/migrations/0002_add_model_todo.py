# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Todo'
        db.create_table(u'todo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('is_done', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('todolist', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='todos', null=True, to=orm['core.TodoList'])),
        ))
        db.send_create_signal('core', ['Todo'])


    def backwards(self, orm):
        # Deleting model 'Todo'
        db.delete_table(u'todo')


    models = {
        'core.todo': {
            'Meta': {'object_name': 'Todo', 'db_table': "u'todo'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_done': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'todolist': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'todos'", 'null': 'True', 'to': "orm['core.TodoList']"})
        },
        'core.todolist': {
            'Meta': {'object_name': 'TodoList', 'db_table': "u'todolist'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        }
    }

    complete_apps = ['core']