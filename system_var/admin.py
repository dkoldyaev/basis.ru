__author__ = 'dkoldyaev'

from django.contrib import admin
from django.db.models import ImageField

from .models import Var
from basis.widgets import ImageWidget

class VarAdmin(admin.ModelAdmin):

    fieldsets = [
        (None,      {'fields':  ['name', 'group', 'slug']}),
        (None,      {'fields':  ['integer', 'string', 'text', 'image']}),
        (None,      {'fields':  ['comment']}),
        ('Admin',   {'fields':  ['_created', '_updated', '_active', '_comment'],
                     'classes': ['collapse']}),
    ]

    readonly_fields = ['_created', '_updated']

    list_display = ['name', 'slug', 'group', 'value']
    list_filter = ['group']
    formfield_overrides = {
        ImageField:     {'widget':  ImageWidget()}
    }

admin.site.register(Var, VarAdmin)
