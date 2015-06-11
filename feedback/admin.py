__author__ = 'dkoldyaev'

from django.contrib import admin

from feedback.models import Feedback, OrderCall

admin.site.register(Feedback)
admin.site.register(OrderCall)