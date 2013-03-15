#!/usr/bin/env python
# encoding: utf-8
"""
forms.py

Created by Luan Fonseca de Farias on 2013-03-14.
Copyright (c) 2013 Multmeio [design+tecnologia]. All rights reserved.
"""

from django import forms

from core.models import *

class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'input-text',
                'placeholder': 'Name of the new List.',
                'required': 'required',
                'autofocus': 'autofocus'
            })
        }


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        excludes = ['todolist']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'input-text',
                'placeholder': 'Name of the new Todo.',
                'required': 'required',
                'autofocus': 'autofocus'
            })
        }

    def save(self, todolist=None, commit=True, *args, **kwargs):
        """
        Method override to make the criation of
        a Todo more consistent, because we always
        is need to pass the TodoList instance, related with
        this Todo. So we pass that instance for argument
        to this method.
        """
        instance = super(TodoForm, self).save(commit=False, *args, **kwargs)
        instance.todolist = todolist
        if commit:
            instance.save()
        return instance

