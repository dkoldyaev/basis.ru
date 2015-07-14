__author__ = 'dkoldyaev'

from django.contrib import admin
from django.utils.safestring import mark_safe
from django.db import models

from suit.admin import SortableTabularInline

from planing.models import Apartment, Building
from basis.widgets import SVGImageWidget

class ApartmentInlineAdmin(SortableTabularInline):

    model = Apartment
    fields = ['plan_fill', 'plan', 'price', 'description',]
    extra = 0

    formfield_overrides = {
        models.FileField:   {'widget':  SVGImageWidget()}
    }

class BuildingAdmin(admin.ModelAdmin):

    fieldsets = [
        (None,          {'fields':  ['name', 'plan', 'description',]}),
        ('Admin',       {'fields':  ['_created', '_updated', '_active', '_comment'],
                         'classes': ['collapse']}),
        # ('Meta',        {'fields':  ['meta_title', 'meta_description', 'meta_keywords'],
        #                  'classes': ['collapse']}),
    ]

    readonly_fields = ['_created', '_updated', ]

    inlines = [ApartmentInlineAdmin]

    formfield_overrides = {
        models.FileField:   {'widget':  SVGImageWidget()}
    }

admin.site.register(Building, BuildingAdmin)
# admin.site.register(Apartment)