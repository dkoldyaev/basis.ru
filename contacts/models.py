# -*- coding: utf-8 -*-
__author__ = 'dkold_000'

from django.db import models
from ckeditor.fields import RichTextField

from basis.models import BaseModel
from contacts.managers import ContactQuerySet

class Contact(BaseModel):

    slug =      models.SlugField(blank=True, null=False, verbose_name=u'URL')

    image =     models.ImageField(blank=True, null=True, verbose_name=u'Фоновое изображение')
    text =      RichTextField(blank=True, null=True, verbose_name=u'Текст', config_name='medium')
    coord =     models.CharField(blank=False, null=False, max_length=255, verbose_name=u'Координаты маркера')
    coord_popup=RichTextField(blank=False, null=False, verbose_name=u'Текст на всплывающей подсказке маркера')

    objects =   ContactQuerySet.as_manager()