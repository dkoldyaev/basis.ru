__author__ = 'dkoldyaev'

from django.contrib import admin

from feedback.models import Feedback, OrderCall

class FeedbackAdmin(admin.ModelAdmin):

    fieldsets = [
        (None,          {'fields':['page']}),
        (None,          {'fields':['name', 'email', 'phone', 'message']}),
        ('Admin',       {'fields':  ['_created', '_updated', '_active', '_comment'],
                         'classes': ['collapse']}),
    ]
    readonly_fields = ['_created', '_updated', 'page']

class OrderCallAdmin(admin.ModelAdmin):

    fieldsets = [
        (None,          {'fields':['page']}),
        (None,          {'fields':['phone',]}),
        ('Admin',       {'fields':  ['_created', '_updated', '_active', '_comment'],
                         'classes': ['collapse']}),
    ]
    readonly_fields = ['_created', '_updated', 'page']

admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(OrderCall, OrderCallAdmin)