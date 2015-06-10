__author__ = 'dkoldyaev'

from django.contrib import admin

from suit.admin import SortableTabularInline

from planing.models import Apartment, Building

class ApartmentInlineAdmin(SortableTabularInline):

    model = Apartment
    fields = ['plan', 'price', 'description']
    extra = 0

class BuildingAdmin(admin.ModelAdmin):

    inlines = [ApartmentInlineAdmin]

admin.site.register(Building, BuildingAdmin)
# admin.site.register(Apartment)