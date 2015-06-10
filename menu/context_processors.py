__author__ = 'dkoldyaev'

def menu_items(request) :

    from .models import HeaderMenuItem, FooterMenuItem

    try:    current_header_menu_item = HeaderMenuItem.objects.get_active(path__iexact=request.path, hide_not_active=not request.user.is_staff)
    except: current_header_menu_item = None

    try:    parent_header_menu_item =  HeaderMenuItem.objects.get_active(path__istartswith=request.path, hide_not_active=not request.user.is_staff)
    except: parent_header_menu_item =  None

    try:    current_footer_menu_item = FooterMenuItem.objects.get_active(path__iexact=request.path, hide_not_active=not request.user.is_staff)
    except: current_footer_menu_item = None

    try:    parent_footer_menu_item =  FooterMenuItem.objects.get_active(path__istartswith=request.path, hide_not_active=not request.user.is_staff)
    except: parent_footer_menu_item =  None

    return {

        'header_menu_items':        HeaderMenuItem.objects.all_active(hide_not_active=not request.user.is_staff),
        'current_header_menu_item': current_header_menu_item,
        'parent_header_menu_item':  parent_header_menu_item,

        'footer_menu_items':        FooterMenuItem.objects.all_active(hide_not_active=not request.user.is_staff),
        'current_footer_menu_item': current_footer_menu_item,
        'parent_footer_menu_item':  parent_footer_menu_item,

    }