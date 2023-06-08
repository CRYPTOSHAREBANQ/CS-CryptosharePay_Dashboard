# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm, LoginConfirmationForm, Login_individual_Form,BussinessSelectForm, BusinessSignupForm, UploadDocumentForm
from django.http import HttpResponse
from django.template import loader

from utils.cryptosharepay import CryptoSharePay
from utils.cryptosharepay_utils import CryptoSharePayUtils

from core.settings import GITHUB_AUTH

from utils.decorators import is_logged, is_not_logged, is_logged_business

from utils.constants.cryptosharepay_constants import SUPPORTED_COUNTRIES_LIST

from utils.general.s3_manager import S3Manager

from datetime import datetime

def index(request):
    context = {'segment': 'index'}

    return render(request, "index/home.html", context)

@is_not_logged
def signup_business(request):
    form = BusinessSignupForm(request.POST or None)
    context = {
        'form': form,
        "msg": None,
        "countries": SUPPORTED_COUNTRIES_LIST
    }

    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            country_id = form.cleaned_data.get('country_id')
            business_name = form.cleaned_data.get('business_name')
            business_description = form.cleaned_data.get('business_description')

            birthdate = form.cleaned_data.get('birthdate')
            # business_document = form.cleaned_data.get('business_document')
            
            print("TEST")
            # return render(request, "accounts/signup_business.html", context)

            cryptosharepay_utils = CryptoSharePayUtils()
            account_creation_response = cryptosharepay_utils.create_account_business(email, password, confirm_password, first_name, last_name, country_id, birthdate, business_name, business_description)
            print(account_creation_response)

            if account_creation_response['status'] != 'SUCCESS':
                context["msg"] = account_creation_response["message"]

                return render(request, "accounts/signup_business.html", context)

            messages.success(request, 'Account created successfully')
            return redirect('authentication:login')
        else:
            print("ERROR")
            messages.error(request, 'Please correct the error below.')

    return render(request, "accounts/signup_business.html", context)

@is_not_logged
def signup_individual(request):

    context = {   
        "countries": SUPPORTED_COUNTRIES_LIST
    }


    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        cedula = request.POST.get('cedula')
        birthdate = request.POST.get('birthday')
        identity = request.POST.get('identity')
        password = request.POST.get('password')
        cryptosharepay_utils = CryptoSharePayUtils()
        birthdate = datetime.strptime(birthdate, '%m/%d/%Y').strftime('%m/%d/%Y')

        account_creation_response = cryptosharepay_utils.create_indivisual_user(name , email, phone,country,cedula,birthdate,identity,password)

        if account_creation_response['status'] != 'SUCCESS':
            

            return render(request, "accounts/signup_individual.html")

        messages.success(request, 'Account created successfully')
        
        return redirect('authentication:login_individual')
    else:
        print("ERROR")
        messages.error(request, 'Please correct the error below.')

    return render(request, "accounts/signup_individual.html",context)





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
def Individual_login_view(request):
    form = Login_individual_Form(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")

            cryptosharepay_utils = CryptoSharePayUtils()
            response = cryptosharepay_utils.request_individual_login_dashboard(username)

            if response["status"] != "SUCCESS":
                # messages.info(request, "Invalid credentials")
                msg = 'Invalid credentials'
            else:
                login_confirmation_form = LoginConfirmationForm(
                    initial={
                        "username": username
                    }
                )

                return render(request, "accounts/login_confirmation_individual.html", {"form": login_confirmation_form, "msg": msg})
                # return redirect("/")

            
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login_individual.html", {"form": form, "msg": msg})








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



@is_not_logged
def Individual_login_confirmation(request):

    # if request.method == "GET":
    #     return redirect("authentication:login")

    form = LoginConfirmationForm(request.POST or None)

    msg = None

    if form.is_valid():
        username = form.cleaned_data.get("username")
        security_password = form.cleaned_data.get("security_password")

        cryptosharepay_utils = CryptoSharePayUtils()
        response = cryptosharepay_utils.login_dashboard_individual(username, security_password)

        if response["status"] != "SUCCESS":
            msg = response["message"]
            return render(request, "accounts/signup_individual.html", {"form": form, "msg": msg})

        else:
            data = response["data"]

            
            account_customer_id = data["customer_id"]

            request.session["account_email"] = username
            request.session["customer_id"] = account_customer_id
            request.session["is_logged"] = True
            request.session["type"] = "individual"

        
        return redirect("home:dashboard")
        # return redirect("/dashboard.html")
    
    return redirect("/")




# @is_logged
@is_logged_business
def select_business(request):
    # request.session.clear
    # if request.session["type"] != "individual":
        print(request.session["account_email"])
        print('customer id ')
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
            else:
                return render(request, "accounts/select_business.html", context)

        return redirect("home:dashboard")
    # else:
        
    #     if request.method == "GET":
    #         form = BussinessSelectForm(request.POST or None)
        
    #         msg = None

    #         context = {
    #         "form": form, 
    #         "msg": msg, 
    #         "businesses": []
    #     }
    #         cryptosharepay_utils = CryptoSharePayUtils()
    #         print(request.session["customer_id"])
    #         print(request.session["account_email"])
    #         response_api_key = cryptosharepay_utils.get_api_key_by_user_id(
    #         request.session["customer_id"],
    #         request.session["account_email"],
            
                    
    #             )
            
    #         if response_api_key["status"] != "SUCCESS":
                
    #             html_template = loader.get_template('home/page-500.html')
    #             # return HttpResponse(html_template.render({"form": form, "msg": msg}, request))
    #         else:
    #             print('inside else ')
    #             response_data = response_api_key["data"]
    #             api_key_data = response_data["api_key"]
    #             if api_key_data is None:
    #                 msg = "No API Key found for this business"
    #                 return render(request, "accounts/login_individual.html")
    #             else:
    #                 api_key = api_key_data["api_key"]
    #                 request.session["active_api_key"] = api_key
    #     else:
    #         return render(request, "accounts/login_individual.html")    
        # return redirect("home:dashboard")

@is_logged
def upload_country_document(request):
    form = UploadDocumentForm(request.POST, request.FILES)
    print(request.FILES)
    if request.method == "GET":
        return render(request, "accounts/upload_country_document.html", {"form": form})
    
    elif request.method == "POST":
        if form.is_valid():
            pass
            
            document_front_name = form.cleaned_data.get("document_front")
            document_front_name_content = request.FILES["document_front"]

            document_back_name = form.cleaned_data.get("document_back")
            document_back_name_content = request.FILES["document_back"]

            s3_manager = S3Manager()
            s3_manager.upload_object_file_to_bucket("cryptosharepay-accounts", f"{request.session['customer_id']}_country_front.png", document_front_name_content, f"country-documents/{request.session['customer_id']}")
            s3_manager.upload_object_file_to_bucket("cryptosharepay-accounts", f"{request.session['customer_id']}_country_back.png", document_back_name_content, f"country-documents/{request.session['customer_id']}")

            print("READY?")

            # upload_file_to_bucket(self, bucket, file_path, destination_path)

        else:
            print("ERROR")
            print(form.errors)

    return render(request, "accounts/upload_country_document.html", {"form": form})
    # UploadDocumentForm
    pass



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
