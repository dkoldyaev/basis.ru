__author__ = 'dkoldyaev'

from django.contrib import admin

from suit.admin import SortableTabularInline

from slide.models import SlidePage, Slide

class SlideAdminInline(SortableTabularInline):

    model = Slide
    fields = ['image', 'title_digit', 'title_line1_text', 'title_line1_deg', 'title_line2_text', 'title_line2_deg', ]
    ordering = ['order']
    extra = 0

class SlidePageAdmin(admin.ModelAdmin):

    inlines = [SlideAdminInline]

admin.site.register(SlidePage, SlidePageAdmin)