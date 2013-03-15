#!/usr/bin/env python
# encoding: utf-8
"""
todo.py

Created by Luan Fonseca de Farias on 2013-03-14.
Copyright (c) 2013 Multmeio [design+tecnologia]. All rights reserved.
"""

from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage

from core.models import TodoList, Todo
from core.forms import TodoListForm, TodoForm


def add(request, todolist_id):
    """
    View created to add a new Todo,
    Receiving an POST request and send it
    to the TodoForm, for beeing saved,
    if the form is valid.
    """
    todolist = get_object_or_404(TodoList, pk=todolist_id)
    todo_form = TodoForm(request.POST or None)

    if todo_form.is_valid():
        todo = todo_form.save(todolist=todolist)
        messages.success(request, u'Todo "%s" created with success.' % todo)
    else:
        messages.error(request, u'The form was not filled correctly.')

    return redirect('todos', todolist_id)


def change_state(request, todolist_id, todo_id):
    """
    View created to change the state of one Todo,
    The State can be changed in True/False,
    representing the state of the Todo,
    if this Todo was resolved or not.
    """
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.change_state()
    messages.success(request, u'Todo "%s" changed with success.' % todo)
    return redirect('todos', todolist_id)


def delete(request, todolist_id, todo_id):
    """
    View created to delete one Todo,
    and returns to the his TodoList page.
    """
    todo = get_object_or_404(Todo, pk=todo_id)
    messages.success(request, u'Todo "%s" removed with success.' % todo)
    todo.delete()
    return redirect('todos', todolist_id)


def list(request, todolist_id, page=1):
    """
    View created to list all the Todos,
    paginated by Five itens per page, and
    display in the last <li> a input for
    add new Todos.
    """
    todolist = get_object_or_404(TodoList, pk=todolist_id)
    paginator = Paginator(todolist.todos.all(), 5)

    try:
        todos = paginator.page(int(page))
    except EmptyPage:
        todos = []

    data = {
        'todolist': todolist,
        'todo_form': TodoForm(),
        'todos': todos,
        'page': page,
    }
    return render_to_response('todos.html', data,
        context_instance=RequestContext(request))
