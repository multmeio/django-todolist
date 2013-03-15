#!/usr/bin/env python
# encoding: utf-8
"""
admin.py

Created by Luan Fonseca de Farias on 2013-03-14.
Copyright (c) 2013 Multmeio [design+tecnologia]. All rights reserved.
"""

from django.contrib import admin
from django.db.models.base import ModelBase

from core.models import *

# Registering the Models for
# they be available in the Admin interface
admin.site.register(TodoList)
admin.site.register(Todo)
