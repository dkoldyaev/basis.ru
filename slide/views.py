__author__ = 'dkoldyaev'

from django.shortcuts import Http404, render

from slide.models import SlidePage

def detail(request, slide_page_slug):

    if not slide_page_slug:
        slide_page_slug = 'index'

    try:
        slide_page =    SlidePage.objects.get_active(hide_not_active=not request.user.is_staff, slug=slide_page_slug)

    except:
        raise Http404

    return render(
        request,
        'slide/page_detail.html',
        {
            'page': slide_page
        }
    )