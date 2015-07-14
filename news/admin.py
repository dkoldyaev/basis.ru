# -*- coding: utf-8 -*-
__author__ = 'dkoldyaev'

from django.db import models
from django.contrib import admin
from django.utils.safestring import mark_safe

from basis.widgets import ImageWidget
from news.models import News

class NewsAdmin(admin.ModelAdmin):

    fieldsets = (
        (None,      {'fields':  ['date', 'title']}),
        (u'Анонс',  {'fields':  ['announce']}),
        (u'Текст',  {'fields':  ['image', 'text']}),
        ('Admin',   {'fields':  ['_created', '_updated', '_active', '_comment'],
                     'classes': ['collapse']}),
    )

    readonly_fields = ['_created', '_updated', ]
    list_display = ['date', 'title', 'get_image']
    list_display_links = ['title', 'get_image']

    def get_image(self, obj):
        if obj.image :
            from basis.templatetags.admin_preview import admin_preview
            return mark_safe('<img src="%s" />' % admin_preview(obj.image.url))
        return ''

    formfield_overrides = {
        models.ImageField:  {'widget':  ImageWidget()}
    }

admin.site.register(News, NewsAdmin)