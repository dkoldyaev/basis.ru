# -- coding: utf-8 --
__author__ = u'Кольдяев Дмитрий'

from django import forms
from django.contrib import admin
from suit.widgets import EnclosedInput

class SlideForm(forms.ModelForm):

    class Meta:
        widgets = {
            'title_width':      EnclosedInput(attrs={'class': 'input-mini'}),
            'title_digit':      EnclosedInput(attrs={'class': 'input-mini'}),

            'title_line1_deg':  EnclosedInput(attrs={'class': 'input-mini'}),
            'title_line1_top':  EnclosedInput(attrs={'class': 'input-mini'}),
            'title_line1_right':EnclosedInput(attrs={'class': 'input-mini'}),

            'title_line2_deg':  EnclosedInput(attrs={'class': 'input-mini'}),
            'title_line2_top':  EnclosedInput(attrs={'class': 'input-mini'}),
            'title_line2_right':EnclosedInput(attrs={'class': 'input-mini'}),
        }