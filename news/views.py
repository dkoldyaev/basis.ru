__author__ = 'dkoldyaev'

import json

from django.shortcuts import render, Http404
from django.template.loader import render_to_string
from django.http import JsonResponse

from news.models import News

def list(request):

    page_size = 10

    try:
        current_page =  int(request.GET.get('page', '1'))
        news = News.objects.filter_active(hide_not_active=not request.user.is_staff)
        next_page = current_page+1 if news.count() > page_size*current_page else None
        news = news[page_size*(current_page-1):page_size*current_page]
        if news.count() == 0 :
            raise
    except:
        raise Http404

    if request.is_ajax() :

        result = {
            'news_data':    render_to_string(
                                'inc/news_list.html',
                                {'news':news}
                            ),
            'current_page': current_page,
            'next_page':    next_page
        }

        return JsonResponse(result)

    return render(
        request,
        'news/list.html',
        {
            'news':         news,
            'current_page': current_page,
            'next_page':    next_page
        }
    )

def detail(request, news_id, news_slug):

    try:
        news = News.objects.get_active(hide_not_active=not request.user.is_staff, id=news_id, slug=news_slug)
    except:
        raise Http404

    return render(
        request,
        'news/detail.html',
        {
            'news_item':     news
        }
    )