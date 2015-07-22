# -- coding: utf-8 --
__author__ = u'Кольдяев Дмитрий'

from django import forms
from django.contrib import admin
from suit.widgets import NumberInput

class SlideForm(forms.ModelForm):

    class Meta:
        widgets = {
            'title_width':      NumberInput(append='px', attrs={'class': 'input-mini'}),
            'title_digit':      NumberInput(attrs={'class': 'input-mini'}),

            'title_line1_deg':  NumberInput(attrs={'class': 'input-mini'}),
            'title_line1_top':  NumberInput(attrs={'class': 'input-mini'}),
            'title_line1_right':NumberInput(attrs={'class': 'input-mini'}),

            'title_line2_deg':  NumberInput(attrs={'class': 'input-mini'}),
            'title_line2_top':  NumberInput(attrs={'class': 'input-mini'}),
            'title_line2_right':NumberInput(attrs={'class': 'input-mini'}),
        }
