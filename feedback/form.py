# -*- coding: utf-8 -*-
__author__ = 'dkoldyaev'

from django import forms
from django.forms import widgets

from feedback.models import Feedback, OrderCall

class FeedbackForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.page.widget = widgets.HiddenInput()

    class Meta:
        model =     Feedback
        fields =    ['name', 'email', 'phone', 'message', 'page']