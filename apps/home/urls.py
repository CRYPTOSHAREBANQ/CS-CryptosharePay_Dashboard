# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

app_name = "home"

urlpatterns = [

    # The home page
    # path('', views.home, name='home'),
    path("test-index/", views.text_index, name="test_index"),
    path("payment-links/", views.create_payment_link, name="payment_links"),
    path("withdrawals/", views.create_withdrawal, name="withdrawals"),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
