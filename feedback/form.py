# -*- coding: utf-8 -*-
__author__ = 'dkoldyaev'

from django.conf import settings
from django import forms
from django.forms import widgets
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMultiAlternatives
from django.core.exceptions import ObjectDoesNotExist

from feedback.models import Feedback, OrderCall

class BaseFeedbackForm(forms.ModelForm):

    def send_email(self, subject):

        if not self.instance :
            raise ObjectDoesNotExist(u'Сохраните форму до отправки email\'а')

        submit_from =   settings.EMAIL_SEND_FROM
        submit_to =     settings.EMAIL_SEND_TO

        data = {'instance': self.instance}

        html_content =  render_to_string(
            'feedback/email/feedback.html',
            data
        )
        text_content =  render_to_string(
            'feedback/email/feedback.html',
            data
        )

        email = EmailMultiAlternatives(
            subject,
            text_content,
            submit_from,
            submit_to
        )
        email.attach_alternative(html_content, 'text/html')
        email.send()

class FeedbackForm(BaseFeedbackForm):

    class Meta:
        model =     Feedback
        fields =    ['name', 'email', 'phone', 'message', 'page']
        widgets =   {
            'page':     widgets.HiddenInput()
        }

class OrderCallForm(BaseFeedbackForm):

    class Meta:
        model =     OrderCall
        fields =    ['phone', 'page']
        widgets =   {
            'page':     widgets.HiddenInput()
        }