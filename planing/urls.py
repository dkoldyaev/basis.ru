__author__ = 'dkoldyaev'

from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^$', 'planing.views.buildings', name='buildings_list'),
    url(r'^/(?P<building_id>[\d]+)$', 'planing.views.building_detail', name='building_detail'),
    url(r'^/(?P<building_id>[\d]+)/(?P<apartment_id>[\d]+)$', 'planing.views.apartment', name='apartment_detail'),
)
