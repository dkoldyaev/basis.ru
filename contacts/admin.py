# -*- coding: utf-8 -*-
__author__ = 'dkold_000'

from django.db import models
from django.contrib import admin

from basis.widgets import ImageWidget
from contacts.models import Contact

class ContactAdmin(admin.ModelAdmin):

    fieldsets = [
        (None,          {'fields':  ['image', 'text']}),
        (u'Координаты', {'fields':  ['coord', 'coord_popup']}),
        ('Admin',       {'fields':  ['_created', '_updated', '_active', '_comment'],
                         'classes': ['collapse']}),
    ]

    formfield_overrides = {
        models.ImageField:  {'widget':  ImageWidget()}
    }

    readonly_fields = ['_created', '_updated']

admin.site.register(Contact, ContactAdmin)