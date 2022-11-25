# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages


from utils.decorators import is_logged, is_not_logged
from utils.cryptosharepay_utils import CryptoSharePayUtils


from .forms import CreateTransactionDigitalToCryptoForm


@is_logged
def index(request):
    context = {'segment': 'index'}

    return render(request, "home/dashboard.html", context)

@is_logged
def home(request):
    context = {'segment': 'index'}

    return render(request, "home/dashboard.html", context)

def text_index(request):
    context = {'segment': 'index'}

    return render(request, "home/index.html", context)

@is_logged
def create_payment_link(request):
    form = CreateTransactionDigitalToCryptoForm(request.POST or None)

    context = {
        "segment": "payment_links",
        "form": form,
        "digital_currencies": []
    }   

    if request.method == "GET":
        cryptosharepay_utils = CryptoSharePayUtils(api_key = "tsk_e2deefd547179e2e15ad62f16fb8b00e")

        digital_currencies_response = cryptosharepay_utils.get_digital_currencies()
        if digital_currencies_response["status"] != "SUCCESS":
            html_template = loader.get_template('home/page-500.html')
            return HttpResponse(html_template.render(context, request))
        else:
            response_data = digital_currencies_response["data"]

            context["digital_currencies"] = response_data["digital_currencies"]

        cryptocurrencies_response = cryptosharepay_utils.get_cryptocurrencies()
        if cryptocurrencies_response["status"] != "SUCCESS":
            html_template = loader.get_template('home/page-500.html')
            return HttpResponse(html_template.render(context, request))
        else:
            response_data = cryptocurrencies_response["data"]

            context["cryptocurrencies"] = response_data["cryptocurrencies"]

        blockchains_response = cryptosharepay_utils.get_blockchains()
        if blockchains_response["status"] != "SUCCESS":
            html_template = loader.get_template('home/page-500.html')
            return HttpResponse(html_template.render(context, request))
        else:
            response_data = blockchains_response["data"]

            context["blockchains"] = response_data["blockchains"]

        return render(request, "transactions/create_transaction_digital_to_crypto.html", context)
    
    elif request.method == "POST":

        if form.is_valid():
            # print(form)
            print(messages)

            pass
        else:
            msg = 'Error validating the form'
            messages.error(request, "Invalid fields")


        return redirect("home:payment_links")

@is_logged
def create_withdrawal(request):
    form = CreateTransactionDigitalToCryptoForm(request.POST or None)

    context = {
        "segment": "withdrawals",
        "form": form,
    }   

    return render(request, "transactions/create_transaction_withdrawal.html", context)

@is_logged
def pages(request):
    print(request.session["businesses"], request.session["active_business"])
    print(request.session["active_api_key"], request.session["account_email"])
    print(request.session["customer_id"])
    # print(request.session["customer_id"], request.session["is_logged"])
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
