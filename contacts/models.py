# -*- coding: utf-8 -*-
__author__ = 'dkold_000'

from django.db import models
from ckeditor.fields import RichTextField

from basis.models import BaseModel
from contacts.managers import ContactQuerySet

class Contact(BaseModel):

    slug =      models.SlugField(blank=True, null=False, verbose_name=u'URL')

    image =     models.ImageField(blank=True, null=True, verbose_name=u'Фоновое изображение')
    text =      RichTextField(blank=True, null=True, verbose_name=u'Текст')
    map_code =  models.TextField(blank=True, null=True, verbose_name=u'Код для встраивания карты')