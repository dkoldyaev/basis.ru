__author__ = 'dkoldyaev'

from django.contrib import admin

from news.models import News

admin.site.register(News)