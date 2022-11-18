# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms

class CreateTransactionDigitalToCryptoForm(forms.Form):
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Transaction description",
                "class": "form-control"
            }
        ),
        max_length = 100
    )

    digital_currency_code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Digital Currency Code",
                "class": "form-control"
            }
        ),
    )

    digital_currency_amount = forms.FloatField(
        widget = forms.DecimalField(
            # attrs={
            #     "placeholder": "Digital Currency Amount",
            #     "class": "form-control"
            # },
            max_digits=14, 
            decimal_places=2
        )
    )

    cryptocurrency_code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Cryptocurrency Code",
                "class": "form-control"
            }
        ),
    )

    cryptocurrency_blockchain_id = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "placeholder": "Cryptocurrency Blockchain ID",
                "class": "form-control"
            }
        ),
    )
    

    
# class LoginConfirmationForm(forms.Form):
#     username = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "placeholder": "Username",
#                 "class": "form-control"
#             }
#         ))
#     password = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "placeholder": "Password",
#                 "class": "form-control"
#             }
#         ))

#     password = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "placeholder": "Password",
#                 "class": "form-control"
#             }
#         ))

#     security_pin = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "placeholder": "Security Pin",
#                 "class": "form-control"
#             }
#         ))