# -*- coding: utf-8 -*-
__author__ = 'dkoldyaev'

from django.contrib import admin
from django.utils.safestring import mark_safe

from suit.admin import SortableModelAdmin
from .models import MenuItem, HeaderMenuItem, MENU_TYPES

class MenuItemAdmin(SortableModelAdmin):

    fieldsets = [
        (None,          {'fields':  ['text', 'type', 'path',]}),
    ] + [
        (
            type[1],    {'fields':  type[2] if type[2] else ['%s_no_settings' % type[0],],
                         'classes': ['suit-tab', 'suit-tab-%s' % (type[0]),]
                        }
        ) for type in MENU_TYPES
    ] + [
        ('Addition',    {'fields':  ['title', 'target',],
                         'classes': ['collapse']}),
        ('Admin',       {'fields':  ['_created', '_updated', '_active', '_comment'],
                         'classes': ['collapse']}),
    ] + [
        ('Meta',        {'fields':  ['meta_title', 'meta_description', 'meta_keywords'],
                         'classes': ['collapse']}),
    ]

    list_display = ['id', 'text', 'path', 'order']
    list_display_links = ['id', 'text', 'path', ]
    suit_form_tabs = [(type[0], type[1]) for type in MENU_TYPES]
    readonly_fields = ['_created', '_updated', 'path', 'planing_no_settings', 'news_list_no_settings', 'contacts_no_settings']
    ordering = ['order']

    change_form_template = 'admin/menu_change_form.html'

    def planing_no_settings(self, obj):
        return mark_safe(u'Нечего настраивать')
    planing_no_settings.short_description = ''

    def news_list_no_settings(self, obj):
        return mark_safe(u'Нечего настраивать')
    news_list_no_settings.short_description = ''

    def contacts_no_settings(self, obj):
        return mark_safe(u'Нечего настраивать')
    news_list_no_settings.short_description = ''

class HeaderMenuItemAdmin(MenuItemAdmin):

    pass

class FooterMenuItemAdmin(MenuItemAdmin):

    def __init__(self, *args, **kwargs):

        super(FooterMenuItemAdmin, self).__init__(*args, **kwargs)

        self.fieldsets = [(u'Положение', {'fields':  ['column']})] + self.fieldsets

        self.list_display = ['id', 'text', 'path', 'column', 'order']

        self.ordering = ['column', 'order']


admin.site.register(HeaderMenuItem, HeaderMenuItemAdmin)
