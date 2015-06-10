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

    objects =   BuildingQuerySet.as_manager()

class Apartment(BaseModel):

    plan =      models.ImageField(blank=False, null=False, upload_to='apartment/plan', verbose_name=u'План квартиры')
    price =     models.IntegerField(blank=False, null=False, verbose_name=u'Цена за м²')

    objects =   ApartmentQuerySet.as_manager()