# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm, LoginConfirmationForm, BussinessSelectForm
from django.http import HttpResponse
from django.template import loader

from utils.cryptosharepay import CryptoSharePay
from utils.cryptosharepay_utils import CryptoSharePayUtils

from core.settings import GITHUB_AUTH

from utils.decorators import is_logged, is_not_logged


def index(request):
    context = {'segment': 'index'}

    return render(request, "index/home.html", context)

def signup_business(request):
    pass

    return render(request, "accounts/signup_business.html")

def signup_individual(request):
    pass

    return render(request, "accounts/signup_individual.html")

@is_not_logged
def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")

            cryptosharepay_utils = CryptoSharePayUtils()
            response = cryptosharepay_utils.request_login_dashboard(username)

            if response["status"] != "SUCCESS":
                # messages.info(request, "Invalid credentials")
                msg = 'Invalid credentials'
            else:
                login_confirmation_form = LoginConfirmationForm(
                    initial={
                        "username": username
                    }
                )

                return render(request, "accounts/login_confirmation.html", {"form": login_confirmation_form, "msg": msg})
                # return redirect("/")

            
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})

@is_not_logged
def login_confirmation(request):

    if request.method == "GET":
        return redirect("authentication:login")

    form = LoginConfirmationForm(request.POST or None)

    msg = None

    if form.is_valid():
        username = form.cleaned_data.get("username")
        security_password = form.cleaned_data.get("security_password")

        cryptosharepay_utils = CryptoSharePayUtils()
        response = cryptosharepay_utils.login_dashboard(username, security_password)

        if response["status"] != "SUCCESS":
            msg = response["message"]
            return render(request, "accounts/login.html", {"form": form, "msg": msg})

        else:
            data = response["data"]

            
            account_customer_id = data["customer_id"]

            request.session["account_email"] = username
            request.session["customer_id"] = account_customer_id
            request.session["is_logged"] = True

        
        return redirect("authentication:select_business")
        # return redirect("/dashboard.html")
    
    return redirect("/")

@is_logged
def select_business(request):
    form = BussinessSelectForm(request.POST or None)
    
    msg = None

    context = {
        "form": form, 
        "msg": msg, 
        "businesses": []
    }

    if request.method == "GET":
        cryptosharepay_utils = CryptoSharePayUtils()
        response_businesses = cryptosharepay_utils.get_businesses(request.session["account_email"], request.session["customer_id"])

        if response_businesses["status"] != "SUCCESS":
            msg = response_businesses["message"]
            html_template = loader.get_template('home/page-500.html')
            return HttpResponse(html_template.render({"form": form, "msg": msg}, request))
        else:
            data_businesses = response_businesses["data"]

            businesses = data_businesses["businesses"]

            # request.session["active_business"] = None
            request.session["businesses"] = businesses
            context["businesses"] = businesses
        
        return render(request, "accounts/select_business.html", context)
    
    elif request.method == "POST":
        if form.is_valid():
            selected_business = form.cleaned_data.get("selected_business")

            request.session["active_business"] = selected_business

            cryptosharepay_utils = CryptoSharePayUtils()

            response_api_key = cryptosharepay_utils.get_api_key_by_business_id(
                request.session["customer_id"],
                request.session["account_email"],
                request.session["active_business"]
            )
            if response_api_key["status"] != "SUCCESS":
                html_template = loader.get_template('home/page-500.html')
                return HttpResponse(html_template.render({"form": form, "msg": msg}, request))
            else:
                response_data = response_api_key["data"]
                api_key_data = response_data["api_key"]
                if api_key_data is None:
                    msg = "No API Key found for this business"
                    return render(request, "accounts/select_business.html", {"form": form, "msg": msg, "businesses": businesses})
                else:
                    api_key = api_key_data["api_key"]
                    request.session["active_api_key"] = api_key

            return redirect("/dashboard.html")

    



@is_logged
def logout(request):
    del(request.session["is_logged"])
    return redirect("authentication:login")




# def register_user(request):
#     msg = None
#     success = False

#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get("username")
#             raw_password = form.cleaned_data.get("password1")
#             user = authenticate(username=username, password=raw_password)

#             msg = 'Account created successfully.'
#             success = True

#             # return redirect("/login/")

#         else:
#             msg = 'Form is not valid'
#     else:
#         form = SignUpForm()

#     return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})
