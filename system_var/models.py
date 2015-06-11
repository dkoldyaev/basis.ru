# -*- coding: utf-8 -*-
__author__ = 'dkoldyaev'

from django.db import models
from django.core.exceptions import ValidationError

from basis.models import BaseModel

class Var(BaseModel):

    name =          models.CharField(max_length=255, blank=False, null=False, verbose_name=u'Имя переменной')
    slug =          models.SlugField(blank=True, null=False, unique=False, verbose_name=u'Идентификатор переменной', help_text=u'Не меняйте значение этого поля, если не уверены в том, что делаете')
    comment =       models.TextField(blank=True, null=True, verbose_name=u'Комментарий')

    group =         models.CharField(max_length=255, blank=True, null=True)

    integer =       models.IntegerField(blank=True, null=True, verbose_name=u'Числовое значение')
    string =        models.CharField(max_length=255, blank=True, null=True, verbose_name=u'Строковое значение')
    text =          models.TextField(blank=True, null=True, verbose_name=u'Текстовое значение')
    image =         models.ImageField(blank=True, null=True, verbose_name=u'Картинка')

    def __unicode__(self):

        return self.name

    @property
    def value(self):

        if self.integer :
            return self.integer

        if self.string :
            return self.string

        if self.text :
            return self.text

        if self.image :
            return self.image

        return None

    def save(self, *args, **kwargs):

        if not self.slug :
            from pytils.translit import slugify
            self.slug = slugify(self.name)

        super(Var, self).save(*args, **kwargs)

    def clean(self):

        vars_count = 0
        errors = {}

        if self.integer :
            vars_count += 1
            errors['integer'] = [u'Заполните только одно поле']

        if self.string :
            vars_count += 1
            errors['string'] = [u'Заполните только одно поле']

        if self.text :
            vars_count += 1
            errors['text'] = [u'Заполните только одно поле']

        if self.image :
            vars_count += 1
            errors['image'] = [u'Заполните только одно поле']

        if vars_count > 1 :
            raise ValidationError(errors)

        else :
            errors = {}

    class Meta:

        ordering = ['group', 'slug']
        verbose_name = u'Системная переменная'
        verbose_name_plural = u'Системные переменные'