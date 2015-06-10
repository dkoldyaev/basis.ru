__author__ = 'dkoldyaev'

from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^$', 'news.views.list', name='news_list'),
    url(r'^/(?P<news_id>[\d]+)_(?P<news_slug>[\w\d_\-]+)$', 'news.views.detail', name='news_detail'),
)
