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
    price =     models.IntegerField(blank=False, null=False, verbose_name=u'Цена за м²')

    building =  models.ForeignKey('planing.Building', related_name='apartments_set', blank=False, null=False)

    description=RichTextField(blank=False, null=False, verbose_name=u'Описание', help_text=u'Площадь, количество комнат и т.д.')

    order =     models.IntegerField(blank=False, null=False, default=0, verbose_name=u'Сортировка')

    objects =   ApartmentQuerySet.as_manager()

    @property
    def get_coords(self):

        import os
        from xml.etree import ElementTree
        from django.conf import settings

        tree = ElementTree.parse(os.path.join(settings.MEDIA_ROOT, self.plan_fill.url))
        root = tree.getroot();

        polylines = root.findall('polyline')
        polygons = []
        for i, coord in enumerate(polylines):
            if i == len(polylines)-1 :
                polygons[0][1]=coord.strip()
            elif i == 0 :
                polygons.append([coord.strip()])
            else:
                polygons.append(coord.split(' '))

        return polygons

    def get_plan_fill_area(self):
        return self.plan_fill_area.split(';')

    def save(self, *args, **kwargs):

        super(Apartment, self).save(*args, **kwargs)

        import itertools
        self.plan_fill_area = ';'.join([','.join(list(itertools.chain(*coord))) for coord in self.get_coords])
        super(Apartment, self).save(*args, **kwargs)

    class Meta:

        ordering =  ['order']
        verbose_name = u'Планировка квартиры'
        verbose_name_plural = u'Планировки квартиры'