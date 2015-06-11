__author__ = 'dkoldyaev'

from django.shortcuts import Http404, HttpResponse

from system_var.models import Var

def ajax_load(request, slug) :

    try:

        result_text = Var.objects.get_active(
            hide_not_active=not request.user.is_staff,
            slug=slug
        ).value

        return HttpResponse(result_text)

    except :

        pass

    raise Http404