# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect

from utils.decorators import is_logged

from .forms import CreateTransactionDigitalToCryptoForm


@is_logged
def index(request):
    context = {'segment': 'index'}

    return render(request, "home/dashboard.html", context)

@is_logged
def home(request):
    context = {'segment': 'index'}

    return render(request, "home/dashboard.html", context)

@is_logged
def create_payment_link(request):
    form = CreateTransactionDigitalToCryptoForm(request.POST or None)

    context = {
        "segment": "payment_links",
        "form": form
    }   

    if request.method == "GET":
        return render(request, "transactions/create_transaction_digital_to_crypto.html", context)


@is_logged
def pages(request):
    print(request.session["customer_id"], request.session["is_logged"])
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template
        print(load_template)

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
