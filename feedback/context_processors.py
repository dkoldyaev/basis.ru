__author__ = 'dkoldyaev'

from feedback.models import OrderCall
from feedback.form import OrderCallForm, FeedbackForm

def order_call_form(request):

    return {'order_call_form':  OrderCallForm(initial={'page':request.path})}

def feedback_form(request):

    return {'feedback_form':  FeedbackForm(initial={'page':request.path})}