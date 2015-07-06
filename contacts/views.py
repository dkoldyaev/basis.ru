__author__ = 'dkold_000'

from django.shortcuts import Http404, render

from contacts.models import Contact

def detail(request):

    try:
        contact_page = Contact.objects.get_active(hide_not_active=not request.user.is_staff)

    except:
        raise Http404

    return render(
        request,
        'contacts/contacts.html',
        {'contact': contact_page}
    )