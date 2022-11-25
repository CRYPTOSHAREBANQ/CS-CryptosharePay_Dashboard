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
    path('login/', login_view, name="login"),
    path("login-confirmation/", login_confirmation, name="login_confirmation"),
    path("select-business", select_business, name="select_business"),
    path("logout/", logout, name="logout"),
]
