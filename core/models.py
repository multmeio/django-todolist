#!/usr/bin/env python
# encoding: utf-8
"""
models.py

Created by Luan Fonseca de Farias on 2013-03-14.
Copyright (c) 2013 Multmeio [design+tecnologia]. All rights reserved.
"""

from django.db import models

class TodoList(models.Model):
    name = models.CharField(max_length=80, null=False, verbose_name=u"Name")

    class Meta:
        db_table = u"todolist"

    def __unicode__(self):
        return u"#%s - %s" % (self.pk, self.name.title())

    @property
    def todos_state(self):
        return u"%s/%s" % (self.todos.count(), self.todos.filter(is_done=True).count())


class Todo(models.Model):
    name = models.CharField(max_length=80, null=False, verbose_name=u"Name")
    is_done = models.BooleanField(default=False, verbose_name=u'Status')

    # relations
    todolist = models.ForeignKey(TodoList, null=True, blank=True,
                                 related_name='todos', verbose_name=u'List')

    class Meta:
        db_table = u"todo"

    def __unicode__(self):
        return u"#%s - %s" % (self.pk, self.name.title())

    def change_state(self):
        self.is_done = not self.is_done
        self.save()
