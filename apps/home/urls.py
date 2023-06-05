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
    path("dashboard/", views.index, name="dashboard"),
    path("test-index/", views.text_index, name="test_index"),
    path("payment-links/", views.payment_links, name="payment_links"),
    path("payment-links/create/", views.create_payment_link, name="create_payment_link"),
    path("payment-links/information/<str:transaction_id>", views.payment_link_information, name="payment_link_information"),

    path("send-payment/", views.send_payment, name="send_payment"),
    path("balance/", views.balance, name="balance"),

    path("withdrawals/", views.create_withdrawal, name="withdrawals"),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
