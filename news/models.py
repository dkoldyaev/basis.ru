# -- coding: utf-8 --
__author__ = 'dkoldyaev'

import django

from django.db import models
from ckeditor.fields import RichTextField

from basis.models import BaseModel
from news.managers import NewsQuerySet

class News(BaseModel) :

    date =      models.DateField(blank=False, null=False, default=django.utils.timezone.now, verbose_name=u'Дата')
    title =     models.CharField(blank=False, null=False, max_length=255, verbose_name=u'Заголовок')

    announce =  models.TextField(blank=False, null=False, verbose_name=u'Анонс', help_text=u'Будет отображаться в сописке новостей')

    image =     models.ImageField(blank=True, null=True, verbose_name=u'Изображение', help_text=u'Будет отображаться над текстом открытой новости')
    text =      RichTextField(blank=False, null=False, verbose_name=u'Текст')

    objects =   NewsQuerySet.as_manager()