# -- coding: utf-8 --
__author__ = 'dkoldyaev'

import django

from django.db import models
from ckeditor.fields import RichTextField

from basis.models import BaseModel
from news.managers import NewsQuerySet

class News(BaseModel) :

    slug =      models.SlugField(blank=True, null=False)

    date =      models.DateField(blank=False, null=False, default=django.utils.timezone.now, verbose_name=u'Дата')
    title =     models.CharField(blank=False, null=False, max_length=255, verbose_name=u'Заголовок')

    announce =  models.TextField(blank=False, null=False, verbose_name=u'Анонс', help_text=u'Будет отображаться в сописке новостей')

    image =     models.ImageField(blank=True, null=True, upload_to='news/image', verbose_name=u'Изображение', help_text=u'Будет отображаться над текстом открытой новости')
    text =      RichTextField(blank=False, null=False, verbose_name=u'Текст')

    objects =   NewsQuerySet.as_manager()

    class Meta:

        ordering =  ['date']
        verbose_name = u'Новость'
        verbose_name_plural = u'Новости'

    def save(self, *args, **kwargs):

        if not self.slug :
            from pytils.translit import slugify
            self.slug = slugify(self.title)

        super(News, self).save(*args, **kwargs)

    def __unicode__(self):

        return '%s (%s)' % (self.title, str(self.date))