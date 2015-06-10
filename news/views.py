__author__ = 'dkoldyaev'

from django.shortcuts import render, Http404

from news.models import News

def list(request):

    page_size = 10

    try:
        current_page =  request.GET.get('page', 1)
        news = News.objects.filter_active(hide_not_active=not request.user.is_staff)
    except:
        raise Http404

    return render(
        request,
        'news/list.html',
        {
            'news':     news[page_size*(current_page-1):page_size*current_page],
            'page':     current_page if news.count() > page_size*current_page else None,
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