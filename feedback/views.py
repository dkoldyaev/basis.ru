# -*- coding: utf-8 -*-
__author__ = 'dkoldyaev'

from django.shortcuts import render, render_to_response, redirect
from django.http import JsonResponse

from feedback.models import Feedback, OrderCall
from feedback.form import FeedbackForm, OrderCallForm

def feedback(request):

    success = False

    if request.method == 'POST' :

        form = FeedbackForm(request.POST)

        if form.is_valid() :

            success = True
            instance = form.save()
            form.send_email(u'Обратная связь')

            if not request.is_ajax() :
                return redirect(instance.page)

        else :

            return JsonResponse({
                'state':    'error',
                'errors':   form.errors
            })

    else:

        form = FeedbackForm(initial={'page':request.path})

    if request.is_ajax() :
        return JsonResponse({
            'success':success,
        })

    return render(
        request,
        'feedback/feedback.html',
        {
            'form':     form,
            'success':  success
        }
    )

def order_call(request):

    success = False

    if request.method == 'POST' :

        form = OrderCallForm(request.POST)

        if form.is_valid() :

            success = True
            instance = form.save()
            form.send_email(u'Заказ звонка')

            if not request.is_ajax() :
                return redirect(instance.page)

        else :

            return JsonResponse({
                'state':    'error',
                'errors':   form.errors
            })

    return JsonResponse({
        'success':success,
    })

