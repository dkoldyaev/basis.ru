__author__ = 'dkoldyaev'

from django.contrib import admin
from django.db import models

from suit.admin import SortableTabularInline

from slide.models import SlidePage, Slide
from slide.forms import SlideForm
from basis.widgets import ImageWidget

class SlideAdminInline(SortableTabularInline):

    model = Slide
    # fields = ['title_line2_text', 'title_line2_deg', ]
    fieldsets = [
        ('Image',   {'fields':  ['image', 'image_position', 'image_size', ]}),
        ('Digits',  {'fields':  ['title_digit', 'title_width',]}),
        ('Title1',  {'fields':  ['title_line1_text', 'title_line1_deg', 'title_line1_top', 'title_line1_right', ]}),
        ('Title2',  {'fields':  ['title_line2_text', 'title_line2_deg', 'title_line2_top', 'title_line2_right', ]}),
        ('Descr',   {'fields':  ['description', ]}),
    ]
    ordering = ['order']
    extra = 0
    formfield_overrides = {
        models.ImageField:  {'widget':  ImageWidget()}
    }
    form = SlideForm

class SlidePageAdmin(admin.ModelAdmin):

    inlines = [SlideAdminInline]

    formfield_overrides = {
        models.ImageField:  {'widget':  ImageWidget()}
    }

admin.site.register(SlidePage, SlidePageAdmin)