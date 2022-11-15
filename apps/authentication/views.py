# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm, LoginConfirmationForm

from utils.cryptosharepay import CryptoSharePay
from utils.cryptosharepay_utils import CryptoSharePayUtils

from core.settings import GITHUB_AUTH

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")


            # user = authenticate(username=username, password=password)
            # if user is not None:
            #     login(request, user)
            #     return redirect("/")
            # else:
            #     msg = 'Invalid credentials'
            cryptosharepay_utils = CryptoSharePayUtils()
            print(username, password)
            response = cryptosharepay_utils.request_customer_id(username, password)
            if response["status"] != "SUCCESS":
                # messages.info(request, "Invalid credentials")
                msg = 'Invalid credentials'
            else:
                login_confirmation_form = LoginConfirmationForm(None)
                # request.session["is_logged"] = True
                return render(request, "accounts/login_confirmation.html", {"form": login_confirmation_form, "msg": msg})
                # return redirect("/")

            
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})

def login_confirmation(request):

    if request.method == "GET":
        return redirect("authentication:login")

    form = LoginConfirmationForm(request.POST or None)

    msg = None

    if form.is_valid():
        security_pin = form.cleaned_data.get("security_pin")
        print(security_pin)

        request.session["is_logged"] = True
        return redirect("/")
    



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
