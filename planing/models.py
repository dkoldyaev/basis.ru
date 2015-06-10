# -- coding: utf-8 --
__author__ = 'dkoldyaev'

from django.db import models

from ckeditor.fields import RichTextField

from basis.models import BaseModel
from planing.managers import BuildingQuerySet, ApartmentQuerySet

class Building(BaseModel):

    name =      models.CharField(blank=False, null=False, max_length=255, verbose_name=u'Название', help_text=u'Например «Дом №4»')

    images_map= models.TextField(blank=False, null=False, verbose_name=u'Image-map карта планировки этажа')
    description=RichTextField(blank=False, null=False, verbose_name=u'Описание', help_text=u'Количество этажей, площадь жилая/общая, цена и т.д.')

    order =     models.IntegerField(blank=False, null=False, default=0, verbose_name=u'Сортировка')

    objects =   BuildingQuerySet.as_manager()

    class Meta:

        ordering =  ['order']
        verbose_name = u'Дом'
        verbose_name_plural = u'Дома'

class Apartment(BaseModel):

    plan =      models.ImageField(blank=False, null=False, upload_to='apartment/plan', verbose_name=u'План квартиры')
    price =     models.IntegerField(blank=False, null=False, verbose_name=u'Цена за м²')

    building =  models.ForeignKey('planing.Building', related_name='apartments_set', blank=False, null=False)

    description=RichTextField(blank=False, null=False, verbose_name=u'Описание', help_text=u'Площадь, количество комнат и т.д.')

    order =     models.IntegerField(blank=False, null=False, default=0, verbose_name=u'Сортировка')

    objects =   ApartmentQuerySet.as_manager()

    class Meta:

        ordering =  ['order']
        verbose_name = u'Планировка квартиры'
        verbose_name_plural = u'Планировки квартиры'