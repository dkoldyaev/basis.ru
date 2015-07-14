# -*- coding: utf-8 -*-
__author__ = 'dkoldyaev'

from django.db import models

from basis.models import BaseModel
from feedback.managers import FeedbackQuerySet, OrderCallQuerySet

# qwerty123zxcvb

class Feedback(BaseModel):

    name =      models.CharField(blank=False, null=False, max_length=255, verbose_name=u'Имя')
    email =     models.EmailField(blank=True, null=True, max_length=255, verbose_name=u'Email')
    phone =     models.CharField(blank=True, null=True, max_length=255, verbose_name=u'Телефон')

    message =   models.TextField(blank=False, null=False)

    page =      models.CharField(blank=True, null=True, max_length=255, verbose_name=u'Страница сайта')

    objects =   FeedbackQuerySet

    def __unicode__(self):
        return u'Обратная связь: %s, %s (%s)' % (self.name, self.message[:30], self._created.strftime('%d.%m.%Y %H:%M'))

class OrderCall(BaseModel):

    phone =     models.CharField(blank=False, null=False, max_length=255, verbose_name=u'Телефон')

    page =      models.CharField(blank=True, null=True, max_length=255, verbose_name=u'Страница сайта')

    def __unicode__(self):
        return u'Обратная связь: %s (%s)' % (self.phone, self._created.strftime('%d.%m.%Y %H:%M'))
