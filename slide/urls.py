__author__ = 'dkoldyaev'

from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^(?P<slide_page_slug>[\w\d\-_]*)$', 'slide.views.detail', name='slide_page'),
    url(r'^(?P<slide_page_slug>[\w\d\-_]+)#slide_(?P<slide_id>[\d]+)$', 'slide.views.detail', name='slide_detail'),
)
