# -*- coding: utf-8 -*-
__author__ = 'dkoldyaev'

from django.db import models

from ckeditor.fields import RichTextField

from basis.models import BaseModel
from slide.managers import SlideQuerySet, SlidePageQuerySet

class Slide(BaseModel):

    image =     models.ImageField(blank=False, null=False, upload_to='slide/image', verbose_name=u'Изоображение')
    image_position = models.CharField(blank=False, null=False, max_length=255, default='0% 0%', verbose_name=u'Позиция изображения')
    image_size= models.CharField(blank=False, null=False, max_length=255, default='100% 100%', verbose_name=u'Размер изображения')

    title =     RichTextField(blank=False, null=False, config_name='simple', verbose_name=u'Заголовок', help_text=u'Форматированный html-код')
    title_width=models.IntegerField(blank=False, null=False, default=350)

    title_digit =       models.CharField(blank=True, null=True, max_length=5, verbose_name=u'Цифра', help_text=u'Большая зеленая цифра')

    title_line1_text =  RichTextField(blank=True, null=True, max_length=50, config_name='ultra_simple', verbose_name=u'Строка 1', help_text=u'Первая строка описания')
    title_line1_deg =   models.IntegerField(blank=False, null=False, default=0)
    title_line1_top =   models.IntegerField(blank=False, null=False, default=53)
    title_line1_right = models.IntegerField(blank=False, null=False, default=0)

    title_line2_text =  RichTextField(blank=True, null=True, max_length=50, config_name='ultra_simple', verbose_name=u'Строка 2', help_text=u'Вторая строка описания')
    title_line2_deg =   models.IntegerField(blank=False, null=False, default=0)
    title_line2_top =   models.IntegerField(blank=False, null=False, default=-45)
    title_line2_right = models.IntegerField(blank=False, null=False, default=0)

    description=RichTextField(blank=True, null=True, config_name='simple', verbose_name=u'Описание', help_text=u'Выводится по нажатию на кнопку «подробнее». Можно оставить пустым')

    page =      models.ForeignKey('slide.SlidePage', blank=False, null=False, related_name='slide_set')

    order =     models.IntegerField(blank=False, null=False, default=0, verbose_name=u'Сортировка')

    objects =   SlideQuerySet.as_manager()

    class Meta:

        ordering =  ['order']
        verbose_name = u'Слайд'
        verbose_name_plural = u'Слайды'

class SlidePage(BaseModel) :

    name =      models.CharField(blank=False, null=False, max_length=255, verbose_name=u'Название группы слайдов')
    slug =      models.SlugField(blank=True, null=False)

    objects =   SlidePageQuerySet.as_manager()

    class Meta:

        verbose_name = u'Группа слайдов'
        verbose_name_plural = u'Группы слайдов'