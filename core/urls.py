#!/usr/bin/env python
# encoding: utf-8
"""
urls.py

Created by Luan Fonseca de Farias on 2013-03-14.
Copyright (c) 2013 Multmeio [design+tecnologia]. All rights reserved.
"""

from django.conf.urls import patterns, include, url

urlpatterns = patterns('core.views',
    # TodoLlists
    url(regex=r'^todolist/add/?$',
        view='todolist.add', name='todolist_add',
    ),
    url(regex=r'^todolist/(?P<todolist_id>\d+)/delete/?$',
        view='todolist.delete', name='todolist_delete',
    ),
    url(regex=r'^/?$',
        view='todolist.list', name='todolists',
    ),
    url(regex=r'^todolists/?$',
        view='todolist.list', name='todolists',
    ),
    url(regex=r'^todolists/page=(?P<page>\d+)/?$',
        view='todolist.list', name='todolists',
    ),

    # Todos
    url(regex=r'^todolist/(?P<todolist_id>\d+)/todo/add/?$',
        view='todo.add', name='todo_add',
    ),
    url(regex=r'^todolist/(?P<todolist_id>\d+)/todo/(?P<todo_id>\d+)/change/state/?$',
        view='todo.change_state', name='todo_change_state',
    ),
    url(regex=r'^todolist/(?P<todolist_id>\d+)/todo/(?P<todo_id>\d+)/delete/?$',
        view='todo.delete', name='todo_delete',
    ),
    url(regex=r'^todolist/(?P<todolist_id>\d+)/todos/?$',
        view='todo.list', name='todos',
    ),
    url(regex=r'^todolist/(?P<todolist_id>\d+)/todos/page=(?P<page>\d+)/?$',
        view='todo.list', name='todos',
    ),
)
