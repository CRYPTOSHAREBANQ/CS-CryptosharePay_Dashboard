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
        widget=forms.Select(
            attrs={
                "placeholder": "Digital Currency Code",
                "class": "form-control"
            }
        ),
    )

    digital_currency_amount = forms.FloatField(
        widget = forms.NumberInput(
            attrs={
                "placeholder": "Digital Currency Amount",
                "class": "form-control"
            },
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

    # cryptocurrency_blockchain_id = forms.CharField(
    #     widget = forms.TextInput(
    #         attrs={
    #             "placeholder": "Cryptocurrency Blockchain ID",
    #             "class": "form-control"
    #         }
    #     ),
    # )

    withdrawal_address = forms.CharField(
        required=False,
        widget = forms.TextInput(
            attrs={
                "placeholder": "Withdrawal Address (OPTIONAL)",
                "class": "form-control"
            }
        ),
    )
    

class CreateWithdrawal(forms.Form):
    cryptocurrency_code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Cryptocurrency Code",
                "class": "form-control"
            }
        ),
    )

    cryptocurrency_amount = forms.FloatField(
        widget = forms.NumberInput(
            attrs={
                "placeholder": "Cryptocurrency Amount",
                "class": "form-control"
            },
        )
    )

    receiver_address = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "placeholder": "Withdrawal Address",
                "class": "form-control"
            }
        ),
    )

    extra_data = forms.CharField(
        required=False,
        widget = forms.TextInput(
            attrs={
                "placeholder": "Extra data (like XRP tag) [OPTIONAL]",
                "class": "form-control"
            }
        )
        
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