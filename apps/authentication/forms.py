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
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    
class LoginConfirmationForm(forms.Form):
    security_pin = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Security Pin",
                "class": "form-control"
            }
        ))