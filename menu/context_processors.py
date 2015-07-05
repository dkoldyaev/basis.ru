__author__ = 'dkoldyaev'

def menu_items(request) :

    from .models import HeaderMenuItem

    try:    current_header_menu_item = HeaderMenuItem.objects.get_active(path__iexact=request.path, hide_not_active=not request.user.is_staff)
    except: current_header_menu_item = None

    parent_header_menu_items =  HeaderMenuItem.objects.none()
    path = request.path

    while (len(path) > 1 and parent_header_menu_items.count() == 0) :
        try:
            path = '/'.join(path.split('/')[:-1])
            parent_header_menu_items |= HeaderMenuItem.objects.filter_active(path__iexact=path, hide_not_active=not request.user.is_staff)
        except:
            pass

    return {

        'header_menu_items':        HeaderMenuItem.objects.all_active(hide_not_active=not request.user.is_staff),
        'current_header_menu_item': current_header_menu_item,
        'parent_header_menu_items': parent_header_menu_items,

    }