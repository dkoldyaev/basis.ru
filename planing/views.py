# -- coding: utf-8 --
__author__ = 'dkoldyaev'

from django.shortcuts import render, Http404, redirect

from planing.models import Building, Apartment

def buildings(request):

    try:
        # редиректим на певый попавшийся дом
        redirect('building_detail', building_id=Building.objects.filter_active(hide_not_active=not request.user.is_staff)[0].id)
    except:
        raise Http404

def building_detail(request, building_id) :

    buildings_list= Building.objects.filter_active(hide_not_active=not request.user.is_staff)

    try:
        building = buildings_list.get(id=building_id)
    except:
        raise Http404

    return render(
        request,
        'planing/building_detail.html',
        {
            'current_building':     building,
            'buildings_list':       buildings_list,
        }
    )

def apartment(request, building_id, apartment_id) :

    try:
        apart = Apartment.objects.get_active(
            hide_not_active=not request.user.is_staff,
            id=apartment_id,
            building__id=building_id)
    except:
        raise Http404

    return render(
        request,
        'planing/apartament_detail.html',
        {
            'apartment':    apart
        }
    )
