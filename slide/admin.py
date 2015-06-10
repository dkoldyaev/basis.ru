__author__ = 'dkoldyaev'

from django.contrib import admin

from slide.models import SlidePage, Slide

admin.site.register(Slide)
admin.site.register(SlidePage)