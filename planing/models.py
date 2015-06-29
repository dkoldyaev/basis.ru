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
    plan =      models.FileField(blank=False, null=True, upload_to='building/plan', verbose_name=u'Планировка этажа')

    order =     models.IntegerField(blank=False, null=False, default=0, verbose_name=u'Сортировка')

    objects =   BuildingQuerySet.as_manager()

    class Meta:

        ordering =  ['order']
        verbose_name = u'Дом'
        verbose_name_plural = u'Дома'

class Apartment(BaseModel):

    plan_fill = models.FileField(blank=False, null=True, upload_to='apartment/plan_fill', verbose_name=u'Заливка при наведении')
    plan_fill_area =\
                models.TextField(blank=True, null=True, verbose_name=u'Координаты области')
    plan =      models.FileField(blank=False, null=True, upload_to='apartment/plan', verbose_name=u'План квартиры')
    price =     models.IntegerField(blank=True, null=True, verbose_name=u'Цена за м²')

    building =  models.ForeignKey('planing.Building', related_name='apartments_set', blank=False, null=False)

    description=RichTextField(blank=True, null=True, config_name='ultra_simple', verbose_name=u'Описание', help_text=u'Площадь, количество комнат и т.д.')

    order =     models.IntegerField(blank=False, null=False, default=0, verbose_name=u'Сортировка')

    objects =   ApartmentQuerySet.as_manager()

    def get_plan_fill_areas(self):
        return self.plan_fill_area.split(';')

    def save(self, *args, **kwargs):

        super(Apartment, self).save(*args, **kwargs)

        from xml.dom import minidom
        doc = minidom.parseString(self.plan_fill.read())
        polylines = doc.getElementsByTagName('polyline')
        self.plan_fill_area = ';'.join([polyline.getAttribute('points').strip().replace(' ', ',') for polyline in polylines])

        super(Apartment, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.id)

    class Meta:

        ordering =  ['order']
        verbose_name = u'Планировка квартиры'
        verbose_name_plural = u'Планировки квартиры'