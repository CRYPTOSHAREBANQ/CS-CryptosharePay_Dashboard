# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, include
# from .views import login_view, register_user
from .views import *

app_name = "authentication"

urlpatterns = [
    path('login/', login_view, name="login"),
    path("login-confirmation/", login_confirmation, name="login_confirmation"),
    path("logout/", logout, name="logout"),
]
