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

from utils.constants.cryptosharepay_constants import SUPPORTED_CRYPTOCURRENCIES, SUPPORTED_CRYPTOCURRENCIES_LIST, SUPPORTED_BLOCKCHAINS, SUPPORTED_BLOCKCHAINS_LIST
from utils.decorators import is_logged, is_not_logged
from utils.cryptosharepay_utils import CryptoSharePayUtils


from .forms import CreateTransactionDigitalToCryptoForm, CreateWithdrawal


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
def payment_links(request):
    context = {
        "segment": "payment_links",
        "transactions": []
    }

    cryptosharepay_utils = CryptoSharePayUtils(api_key = request.session["active_api_key"])

    transactions_response = cryptosharepay_utils.get_all_payment_transactions()
    if transactions_response["status"] != "SUCCESS":
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
    
    response_data = transactions_response["data"]
    transactions = response_data["transactions"]

    context["transactions"] = transactions

    return render(request, "payment_links/payment_links.html", context)
    pass

@is_logged
def create_payment_link(request):
    form = CreateTransactionDigitalToCryptoForm(request.POST or None)

    context = {
        "segment": "payment_links",
        "form": form,
        "digital_currencies": []
    }   

    if request.method == "GET":
        cryptosharepay_utils = CryptoSharePayUtils(api_key = request.session["active_api_key"])

        digital_currencies_response = cryptosharepay_utils.get_digital_currencies()
        if digital_currencies_response["status"] != "SUCCESS":
            html_template = loader.get_template('home/page-500.html')
            return HttpResponse(html_template.render(context, request))
        else:
            response_data = digital_currencies_response["data"]

            context["digital_currencies"] = response_data["digital_currencies"]

        # cryptocurrencies_response = cryptosharepay_utils.get_cryptocurrencies()
        # if cryptocurrencies_response["status"] != "SUCCESS":
        #     html_template = loader.get_template('home/page-500.html')
        #     return HttpResponse(html_template.render(context, request))
        # else:
        #     response_data = cryptocurrencies_response["data"]

        #     context["cryptocurrencies"] = response_data["cryptocurrencies"]

        context["cryptocurrencies"] = SUPPORTED_CRYPTOCURRENCIES_LIST

        # blockchains_response = cryptosharepay_utils.get_blockchains()
        # if blockchains_response["status"] != "SUCCESS":
        #     html_template = loader.get_template('home/page-500.html')
        #     return HttpResponse(html_template.render(context, request))
        # else:
        #     response_data = blockchains_response["data"]

        #     context["blockchains"] = response_data["blockchains"]

        # context["blockchains"] = SUPPORTED_BLOCKCHAINS_LIST


        return render(request, "transactions/create_transaction_digital_to_crypto.html", context)
    
    elif request.method == "POST":

        if form.is_valid():

            cryptosharepay_utils = CryptoSharePayUtils(api_key = request.session["active_api_key"])

            description = form.cleaned_data.get("description")
            digital_currency_code = form.cleaned_data.get("digital_currency_code")
            digital_currency_amount = form.cleaned_data.get("digital_currency_amount")
            cryptocurrency_code = form.cleaned_data.get("cryptocurrency_code")
            cryptocurrency_blockchain_id = SUPPORTED_CRYPTOCURRENCIES[cryptocurrency_code]["blockchain"]

            withdrawal_address = form.cleaned_data.get("withdrawal_address")

            # print("description: ", description)
            # print("digital_currency_code: ", digital_currency_code)
            # print("digital_currency_amount: ", digital_currency_amount)
            # print("cryptocurrency_code: ", cryptocurrency_code)
            # print("cryptocurrency_blockchain_id: ", cryptocurrency_blockchain_id)
            # print("withdrawal_address: ", withdrawal_address)

            create_transaction_digital_to_crypto_response = cryptosharepay_utils.create_digital_transaction_digital_to_crypto(
                description,
                digital_currency_code,
                digital_currency_amount,
                cryptocurrency_code,
                cryptocurrency_blockchain_id,
                withdrawal_address
            )

            if create_transaction_digital_to_crypto_response["status"] != "SUCCESS":
                html_template = loader.get_template('home/page-500.html')
                return HttpResponse(html_template.render(context, request))
            else:
                response_data = create_transaction_digital_to_crypto_response["data"]

            return redirect("home:payment_link_information", transaction_id = response_data["transaction_id"])
        else:
            msg = 'Error validating the form'
            messages.error(request, "Invalid fields")


        return redirect("home:payment_links")

@is_logged
def payment_link_information(request, transaction_id = None):
    context = {
        "segment": "payment_links",
        "transaction": {}
    }

    if transaction_id is None:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
    
    cryptosharepay_utils = CryptoSharePayUtils(api_key = request.session["active_api_key"])
    
    get_transaction_response = cryptosharepay_utils.get_payment_transaction(transaction_id)

    if get_transaction_response["status"] != "SUCCESS":
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
    
    response_data = get_transaction_response["data"]["transaction"]

    context["transaction"] = response_data
    # print(response_data)

    # {
    #     "status": "SUCCESS",
    #     "message": "Transaction retrieved successfully",
    #     "data": {
    #         "transaction": {
    #             "transaction_id": "2d2e542c-3c47-4654-9bbd-a1e4dd0bf1e2",
    #             "transaction_type": "PAYMENT_REQUEST",
    #             "description": "Test transaction4",
    #             "digital_currency_code": "USD",
    #             "digital_currency_amount": 25.0,
    #             "cryptocurrency_code": "BCH",
    #             "cryptocurrency_amount": 0.60328185,
    #             "cryptocurrency_amount_received": null,
    #             "address": "bchtest:qpcdvq7zqrr0q7tc2edn6v3hvfuwj0m9nvgeneurun",
    #             "client_email": "25",
    #             "client_phone": null,
    #             "creation_datetime": 1664423231.927531,
    #             "expiration_datetime": 1664595984.14425,
    #             "status": "CANCELLED"
    #         }
    #     }
    # }

    return render(request, "transactions/information_transaction_digital_to_crypto.html", context)

@is_logged
def create_withdrawal(request):
    form = CreateWithdrawal(request.POST or None)

    context = {
        "segment": "send_payment",
        "form": form,
        "transaction": {}
    }

    context["cryptocurrencies"] = SUPPORTED_CRYPTOCURRENCIES_LIST

    if request.method == "GET":
        return render(request, "transactions/create_transaction_withdrawal.html", context)

    elif request.method == "POST":
        if form.is_valid():

            cryptosharepay_utils = CryptoSharePayUtils(api_key = request.session["active_api_key"])

            cryptocurrency_code = form.cleaned_data.get("cryptocurrency_code")
            cryptocurrency_blockchain_id = SUPPORTED_CRYPTOCURRENCIES[cryptocurrency_code]["blockchain"]
            withdrawal_address = form.cleaned_data.get("receiver_address")
            cryptocurrency_amount = form.cleaned_data.get("cryptocurrency_amount")
            extra_data = form.cleaned_data.get("extra_data")

            create_transaction_withdrawal_response = cryptosharepay_utils.create_transaction_crypto_withdrawal(
                cryptocurrency_code,
                cryptocurrency_blockchain_id,
                withdrawal_address,
                cryptocurrency_amount,
                extra_data
            )

            if create_transaction_withdrawal_response["status"] != "SUCCESS":
                html_template = loader.get_template('home/page-500.html')
                return HttpResponse(html_template.render(context, request))
            
            response_data = create_transaction_withdrawal_response["data"]
            context["transaction"] = response_data

            return redirect("home:withdrawal_information",context)




@is_logged
def pages(request):
    # print(request.session["businesses"], request.session["active_business"])
    # print(request.session["active_api_key"], request.session["account_email"])
    # print(request.session["customer_id"])

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
