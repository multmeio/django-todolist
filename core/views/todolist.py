#!/usr/bin/env python
# encoding: utf-8
"""
todolist.py

Created by Luan Fonseca de Farias on 2013-03-14.
Copyright (c) 2013 Multmeio [design+tecnologia]. All rights reserved.
"""

from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage

from core.models import TodoList, Todo
from core.forms import TodoListForm, TodoForm


def add(request):
    """
    View created to add a new TodoList,
    Receiving an POST request and send it
    to the TodoListForm, for beeing saved,
    if the form is valid.
    """
    todolist_form = TodoListForm(request.POST or None)

    if todolist_form.is_valid():
        todolist = todolist_form.save()
        messages.success(request, u'TodoList "%s" created with success.' % todolist)
    else:
        messages.error(request, u'The form was not filled correctly.')

    return redirect('todolists')


def delete(request, todolist_id):
    """
    View created to delete one TodoList,
    and returns to the TodoLists page.
    """
    todolist = get_object_or_404(TodoList, pk=todolist_id)
    messages.success(request, u'TodoList "%s" removed with success.' % todolist)
    todolist.delete()
    return redirect('todolists')


def list(request, page=1):
    """
    View created to list all the TodoLists,
    paginated by Five itens per page, and
    display in the last <li> a input for
    add new TodoLists.
    """
    paginator = Paginator(TodoList.objects.all(), 5)

    try:
        todolists = paginator.page(int(page))
    except EmptyPage:
        todolists = []

    data = {
        'todolists': todolists,
        'todolist_form': TodoListForm(),
        'page': page
    }
    return render_to_response('todolists.html', data,
        context_instance=RequestContext(request))
