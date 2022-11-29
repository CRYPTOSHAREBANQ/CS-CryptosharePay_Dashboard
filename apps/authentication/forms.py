# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    # password = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "placeholder": "Password",
    #             "class": "form-control"
    #         }
    #     ))
    
class LoginConfirmationForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))

    # password = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "placeholder": "Password",
    #             "class": "form-control"
    #         }
    #     ))

    # security_pin = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "placeholder": "Security Pin",
    #             "class": "form-control"
    #         }
    #     ))

    security_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Security Password",
                "class": "form-control"
            }
        ))

class BussinessSelectForm(forms.Form):
    selected_business = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Business",
                "class": "form-control"
            }
        ))

class BusinessSignupForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your first legal name",
                "class": "form-control"
            }
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your last legal name",
                "class": "form-control"
            }
        )
    )

    business_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your business Name",
                "class": "form-control"
            }
        )
    )

    business_description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your business description",
                "class": "form-control"
            }
        )
    )
    
    country_id = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your native country",
                "class": "form-control"
            }
        )
    )

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your email",
                "class": "form-control"
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Your password",
                "class": "form-control"
            }
        )
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Please confirm your password",
                "class": "form-control"
            }
        )
    )

    birthday = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your birthday",
                "class": "form-control"
            }
        )
    )

    # country_document = forms.FileField(
    #     widget=forms.FileInput(
    #         attrs={
    #             "placeholder": "Your country document",
    #             "class": "form-control"
    #         }
    #     )
    # )




    