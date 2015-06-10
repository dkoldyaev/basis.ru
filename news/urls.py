__author__ = 'dkoldyaev'

from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^$', 'news.views.list', name='news_list'),
    url(r'^/(?P<client_slug>[\w\d\-_]+)$', 'news.views.detail', name='news_detail'),
)
