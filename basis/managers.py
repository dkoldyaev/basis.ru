__author__ = 'dkoldyaev'

from django.db.models import Manager
from django.db.models.query import QuerySet

class BaseQuerySet(QuerySet):

    def get(self, *args, **kwargs):
        if not '_deleted' in kwargs.keys():
            kwargs['_deleted'] = kwargs.pop('_deleted', False)
            kwargs['_active'] = kwargs.pop('_active', True)
        return super(BaseQuerySet, self).get(*args, **kwargs)

    def filter(self, *args, **kwargs):
        if not '_deleted' in kwargs.keys():
            kwargs['_deleted'] = kwargs.pop('_deleted', False)
            kwargs['_active'] = kwargs.pop('_active', True)
        return super(BaseQuerySet, self).filter(*args, **kwargs)

    def all(self):
        return self.filter()

    def get_active(self, *args, **kwargs):
        if kwargs.pop('hide_not_active', True) :
            kwargs['public'] = kwargs.pop('public', True)
        return self.get(*args, **kwargs)

    def filter_active(self, *args, **kwargs):
        if kwargs.pop('hide_not_active', True) :
            kwargs['public'] = kwargs.pop('public', True)
        return self.filter(*args, **kwargs)

    def all_active(self, hide_not_active=True):
        return self.filter_active(hide_not_active=hide_not_active)