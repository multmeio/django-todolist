#!/usr/bin/env python
# encoding: utf-8
"""
tests.py

Created by Luan Fonseca de Farias on 2013-03-14.
Copyright (c) 2013 Multmeio [design+tecnologia]. All rights reserved.
"""

from django.test import TestCase

from core.models import *

TODOLIST_DICT = {
    'name': 'Foobar problems'
}

TODO_DICT = {
    'name': 'First Problem',
    'is_done': False,
}

class TodoListTest(TestCase):
    def setUp(self):
        self.todolist = TodoList.objects.create(**TODOLIST_DICT)
        self.todo_dict = TODO_DICT.copy()
        self.todo_dict.update(todolist=self.todolist)
        self.todo = Todo.objects.create(**self.todo_dict)

    def test_basic_creation(self):
        self.assertEqual(TodoList.objects.count(), 1)

    def test_todos_state(self):
        self.assertEqual(self.todolist.todos_state, '1/0')


class TodoTest(TestCase):
    def setUp(self):
        self.todolist = TodoList.objects.create(**TODOLIST_DICT)
        self.todo_dict = TODO_DICT.copy()
        self.todo_dict.update(todolist=self.todolist)
        self.todo = Todo.objects.create(**self.todo_dict)

    def test_basic_creation(self):
        self.assertEqual(Todo.objects.count(), 1)

    def test_change_state(self):
        self.todo.change_state()
        self.assertEqual(self.todo.is_done, not TODO_DICT['is_done'])

    def test_association_with_todolist(self):
        self.assertEqual(self.todolist.todos.count(), 1)

