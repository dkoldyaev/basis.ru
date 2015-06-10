__author__ = 'dkoldyaev'

from django.contrib import admin

from suit.admin import SortableTabularInline

from slide.models import SlidePage, Slide

class SlideAdminInline(SortableTabularInline):

    model = Slide
    fields = ['image', 'title', 'description',]
    ordering = ['order']
    extra = 0

class SlidePageAdmin(admin.ModelAdmin):

    inlines = [SlideAdminInline]

admin.site.register(SlidePage, SlidePageAdmin)