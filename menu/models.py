# -*- coding: utf-8 -*-
__author__ = 'dkoldyaev'

from django.db import models
from django.core.urlresolvers import reverse

from menu.managers import HeaderMenuQuerySet

from basis.models import BaseModel

MENU_TYPES = [
    ('slide_page',          u'Группа слайдов',          ['slide_page_slide_page',]),
    ('news_list',           u'Список новостей',         []),
    ('planing_build',       u'Планировка дома',         ['planing_build_buildind'])
]
MENU_TARGETS = [
    ('_self',   u'Как обычно'),
    ('_blank',  u'В новой вкладке'),
]

class MenuItem(BaseModel):

    text =      models.CharField(blank=False, null=False, max_length=255, verbose_name=u'Название', help_text=u'Текст, который будет отображаться на пункте меню')
    title =     models.CharField(blank=True, null=False, max_length=255, verbose_name=u'Подсказка', help_text=u'Подсказка, которая будет отображаться при наведении на пункт меню')

    target =    models.CharField(blank=False, null=False, max_length=255, choices=MENU_TARGETS, default=MENU_TARGETS[0][0], verbose_name=u'Тип перехода', help_text=u'Как будет открываться страница при клике на пункт меню')
    path =      models.CharField(blank=False, null=True, max_length=255, default='/', verbose_name=u'URL', help_text=u'Генерируется автоматически')
    type =      models.CharField(blank=False, null=False, default='page', choices=map(lambda t:t[:2], MENU_TYPES), max_length=255, verbose_name=u'Тип', help_text=u'Какая странца должна открываться по клику на пункт меню')
    order =     models.PositiveIntegerField(blank=False, null=False, default=0, verbose_name=u'Сортировка', help_text=u'Для сортировки пунктов в меню. Числа. От большего к меньшему')

    slide_page_slide_page =     models.ForeignKey('slide.SlidePage', blank=True, null=True)
    planing_build_buildind =    models.ForeignKey('planing.Building', blank=True, null=True)

    meta_title =        models.CharField(blank=True, null=True, max_length=255, verbose_name=u'Title', help_text=u'Заголовок окна на странице')
    meta_description =  models.TextField(blank=True, null=True, verbose_name=u'META-Описание', help_text=u'Описание страницы новости для поисковиков')
    meta_keywords =     models.TextField(blank=True, null=True, verbose_name=u'Ключевые слова', help_text=u'Список ключевых слов для поисковиков')

    def get_path(self):

        try:

            if self.type == 'slide_page' :
                if self.slide_page_slide_page.slug == 'index' :
                    return reverse('slide_page', kwargs={'slide_page_slug':''})
                else:
                    return reverse('slide_page', kwargs={'slide_page_slug':self.slide_page_slide_page.slug})

            if self.type == 'news_list' :
                return reverse('news_list')

            if self.type == 'planing_build' :
                return reverse('building_detail', kwargs={'building_id':self.planing_build_buildind.id})

        except :

            pass

        raise ValueError(u'Невозможно сгенерировать url')

    def save(self, *args, **kwargs):

        if not self.title :

            self.title = self.text

        self.path = self.get_path()

        super(MenuItem, self).save(*args, **kwargs)

    def __unicode__(self):

        return '%s: %s (%s)' % (dict(map(lambda mt:mt[:2], MENU_TYPES)).get(self.type), self.text, self.path)

    class Meta:

        abstract = True
        ordering = ['order']
        verbose_name =  u'Пункт меню'
        verbose_name_plural = u'Пункты меню'

class HeaderMenuItem(MenuItem) :

    objects =   HeaderMenuQuerySet.as_manager()

    class Meta:

        verbose_name = u'Пункт меню в шапке сайта'
        verbose_name_plural = u'Пункты меню в шапке сайта'
