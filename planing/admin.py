__author__ = 'dkoldyaev'

from django.contrib import admin

from planing.models import Apartment, Building

admin.site.register(Building)
admin.site.register(Apartment)