import requests
import json
import time
import os

class CryptoSharePay:
    def __init__(self):
        self.BASE = "https://api.cryptosharepay.com/v1"
        self.HEADERS = {
        "Content-Type": "application/json"
        }

    def get_transaction(self, transaction_id):
        url = self.BASE +  f"/protected/transactions/payments/{transaction_id}/"

        response = requests.get(url, headers=self.HEADERS).json()

        return response

    def request_customer_id(self, email, password):
        url = self.BASE + f"/accounts/request-customer-id/"

        headers = {
            "X-Email": email,
            "X-Password": password
        }

        response = requests.post(url, headers=headers)

        return response

    # def generate_coins_transaction_from_address(self, blockchain, network, sending_address, recipient_address, amount):
    #     url = self.BASE + f"/wallet-as-a-service/wallets/{self.WALLET_ID}/{blockchain}/{network}/addresses/{sending_address}/transaction-requests"
    #     data = {
    #             "context": "",
    #             "data": {
    #                 "item": {
    #                     "amount": amount,
    #                     "callbackSecretKey": self.CALLBACK_SECRET_KEY,
    #                     # "callbackUrl": f"{self.CALLBACK_BASE_URL}/cryptoapis/callbacks/ConfirmationsCoinTransactions",
    #                     "feePriority": "standard",
    #                     "note": "",
    #                     "recipientAddress": recipient_address
    #                 }
    #             }
    #         }
        
    #     request = requests.post(url, headers=self.HEADERS, json=data).json()

    #     return request["data"]["item"]
    
    # def generate_coins_transaction_from_wallet(self, blockchain, network, address, amount, data = ""):
    #     url = self.BASE + f"/wallet-as-a-service/wallets/{self.WALLET_ID}/{blockchain}/{network}/transaction-requests"
    #     data = {
    #             "context": "",
    #             "data": {
    #                 "item": {
    #                     "callbackSecretKey": self.CALLBACK_SECRET_KEY,
    #                     "callbackUrl": "https://www.cryptoshareapp.com/atm/ConfirmationsCoinTransactions/",
    #                     "feePriority": "standard",
    #                     "note": data,
    #                     "prepareStrategy": "optimize-size",
    #                     "recipients": [
    #                         {
    #                             "address": address,
    #                             "amount": amount
    #                         }
    #                     ]
    #                 }
    #             }
    #         }

    #     request = requests.post(url, headers=self.HEADERS, json=data).json()

    #     return request["data"]["item"]

