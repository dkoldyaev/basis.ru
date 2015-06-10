# -*- coding: utf-8 -*-
__author__ = 'dkoldyaev'

from django.db import models

from ckeditor.fields import RichTextField

from basis.models import BaseModel
from slide.managers import SlideQuerySet, SlidePageQuerySet

class Slide(BaseModel):

    image =     models.ImageField(blank=False, null=False, upload_to='slide/image', verbose_name=u'Изоображение')
    title =     RichTextField(blank=False, null=False, verbose_name=u'Заголовок', help_text=u'Форматированный html-код')

    description=RichTextField(blank=True, null=True, verbose_name=u'Описание', help_text=u'Выводится по нажатию на кнопку «подробнее». Можно оставить пустым')

    page =      models.ForeignKey('slide.SlidePage', blank=False, null=False, related_name='slide_set')

    objects =   SlideQuerySet.as_manager()

class SlidePage(BaseModel) :

    name =      models.CharField(blank=False, null=False, max_length=255, verbose_name=u'Название группы слайдов')

    objects =   SlidePageQuerySet.as_manager()