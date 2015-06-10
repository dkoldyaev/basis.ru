# -- coding: utf-8 --
__author__ = 'DKOLDYAEV'

from django.db import models
from django.conf import settings

class BaseModel(models.Model):

    public =            models.BooleanField(blank=False, null=False, default=True, verbose_name=u'Отображать на сайте', help_text=u'Если установлено, будет отображаться для всех пользователей. Если снято — только для авторизованных')

    _created =          models.DateTimeField(auto_now_add=True, verbose_name=u'Дата создания')
    _updated =          models.DateTimeField(auto_now=True, verbose_name=u'Дата редактирования')
    _comment =          models.TextField(blank=True, null=True, verbose_name=u'Комментарий')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        

    _active =           models.BooleanField(blank=False, null=False, default=True, verbose_name=u'Опубликовано')
    _deleted =          models.BooleanField(blank=False, null=False, default=False, verbose_name=u'Удалено')

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):

        if settings.SAFE_DELETE :
            self._deleted = True
            self.save()
            from django.db.models import signals
            signals.post_delete.send(sender=self._meta.model, instance=self)

        else :
            super(BaseModel, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        try:
            from pytils.translit import slugify
            if self.slug.strip() == '':
                self.slug = slugify(self.__unicode__())
        except:
            pass

        super(BaseModel, self).save(*args, **kwargs)

    def __unicode__(self):
        try:    return self.name
        except: return '---'

    @property
    def created(self):
        return self._created

    @property
    def updated(self):
        return self._updated

    @property
    def comment(self):
        return self._comment

    @property
    def active(self):
        return self._active