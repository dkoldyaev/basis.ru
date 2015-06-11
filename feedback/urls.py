__author__ = 'dkoldyaev'

from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^$', 'feedback.views.feedback', name='feedback'),
    url(r'^order_call$', 'feedback.views.order_call', name='order_call'),
)
