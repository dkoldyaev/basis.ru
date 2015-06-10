__author__ = 'dkoldyaev'

def menu_items(request) :

    from .models import HeaderMenuItem

    try:    current_header_menu_item = HeaderMenuItem.objects.get_active(path__iexact=request.path, hide_not_active=not request.user.is_staff)
    except: current_header_menu_item = None

    try:    parent_header_menu_item =  HeaderMenuItem.objects.get_active(path__istartswith=request.path, hide_not_active=not request.user.is_staff)
    except: parent_header_menu_item =  None

    return {

        'header_menu_items':        HeaderMenuItem.objects.all_active(hide_not_active=not request.user.is_staff),
        'current_header_menu_item': current_header_menu_item,
        'parent_header_menu_item':  parent_header_menu_item,

    }