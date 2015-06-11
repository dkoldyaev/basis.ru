__author__ = 'dkoldyaev'

from system_var.models import Var

def system_vars(request) :

    variables = Var.objects.filter_active(hide_not_active=not request.user.is_staff).exclude(group='')

    result = {}

    for var in variables :

        try:
            result[var.group][var.slug] = var.value
        except:
            result[var.group] = {var.slug:var.value}

    return result