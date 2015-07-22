# -- coding: utf-8 --
__author__ = u'Кольдяев Дмитрий'

def debug(request):
    from django.conf import settings
    return {'DEBUG':    settings.DEBUG}