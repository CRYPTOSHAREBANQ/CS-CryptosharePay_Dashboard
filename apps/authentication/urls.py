# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, include
# from .views import login_view, register_user
from .views import *

app_name = "authentication"

urlpatterns = [
    path('', index, name='home'),
    path("signup-business/", signup_business, name="signup_business"),
    path("signup-individual/", signup_individual, name="signup_individual"),
    path("upload-country-document/", upload_country_document, name="upload_country_document"),
    path('login/', login_view, name="login"),
    path('login-individual/', Individual_login_view, name="login_individual"),
    
    path("login-confirmation/", login_confirmation, name="login_confirmation"),
    path("login-confirmation-individual/", Individual_login_confirmation, name="login_confirmation_individual"),
    path("select-business/", select_business, name="select_business"),
    path("logout/", logout, name="logout"),
    # path("login-individual/", Individual_login_view, name="login_individual"),
]
