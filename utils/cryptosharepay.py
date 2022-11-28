import requests
import json
import time
import os

class CryptoSharePay:
    def __init__(self, api_key = None):
        self.BASE = "https://api.cryptosharepay.com/v1"
        self.HEADERS = {
        "Content-Type": "application/json"
        }

        if api_key is not None:
            self.HEADERS["X-Api-Key"] = api_key

    def get_cryptocurrencies(self):
        url = self.BASE  + f"/cryptocurrency/supported-cryptocurrencies/"

        headers = {
            "X-Api-key": self.HEADERS["X-Api-Key"]
        }

        response = requests.get(url, headers = self.HEADERS)

        return response

    # NOT AVAILABLE YET
    def get_digital_currencies(self):
        url = self.BASE + f"/digital-currency/supported-digital-currencies/"

        headers = {
            "X-Api-key": self.HEADERS["X-Api-Key"]
        }

        response = requests.get(url, headers = self.HEADERS)

        return response

    def get_payment_transaction(self, transaction_id):
        url = self.BASE +  f"/transactions/payments/{transaction_id}/"

        response = requests.get(url, headers = self.HEADERS)

        return response

    def get_all_payment_transactions(self):
        url = self.BASE + f"/transactions/payments/all/"

        response = requests.get(url, headers = self.HEADERS)

        return response

    def get_blockchains(self):
        url = self.BASE + f"/cryptocurrency/supported-blockchains/"

        response = requests.get(url, headers = self.HEADERS)

        return response

    def get_businesses(self, email, customer_id):
        url = self.BASE + f"/businesses/all/"

        headers = {
            "X-Email": email.lower(),
            "X-Customer-Id": customer_id
        }

        response = requests.get(url, headers=headers)

        return response

    # def get_api_key

    def request_account_customer_id(self, email, password):
        url = self.BASE + f"/accounts/request-customer-id/"

        headers = {
            "X-Email": email.lower(),
            "X-Password": password
        }

        response = requests.post(url, headers=headers)

        return response

    def request_login_dashboard(self, email):
        url = self.BASE + f"/protected/accounts/request-login-dashboard/"

        headers = {
            "X-Email": email.lower()
        }

        response = requests.post(url, headers=headers)

        return response

    def login_dashboard(self, email, security_password):
        url = self.BASE + f"/protected/accounts/login-dashboard/"

        headers = {
            "X-Email": email.lower(),
            "X-Security-Password": security_password
        }

        response = requests.get(url, headers=headers)

        return response

    def get_api_key_by_business_id(self, customer_id, email, business_id):
        url = self.BASE + f"/api-keys/get-by-business-id/?type=PRODUCTION"

        headers = {
            "X-Customer-Id": customer_id,
            "X-Email": email.lower(),
            "X-Business-Id": business_id
        }

        response = requests.get(url, headers=headers)

        return response

    def get_account_customer_id(self, email, password, security_pin):
        url = self.BASE + f"/accounts/account-customer-id/"

        headers = {
            "X-Email": email.lower(),
            "X-Password": password,
            "X-Security-PIN": security_pin
        }

        response = requests.get(url, headers=headers)

        return response
    
    def create_digital_transaction_digital_to_crypto(self, description, digital_currency_code, digital_currency_amount, cryptocurrency_code, cryptocurrency_blockchain_id, withdrawal_address):
        url = self.BASE + f"/transactions/payments/create/digital-to-crypto/"

        headers = {
            "X-Api-key": self.HEADERS["X-Api-Key"]
        }

        body = {
            "data": {
                "description": description,
                "digital_currency_code": digital_currency_code,
                "digital_currency_amount": float(digital_currency_amount),
                "cryptocurrency_code": cryptocurrency_code,
                "cryptocurrency_blockchain_id": cryptocurrency_blockchain_id,
                "withdrawal_address": withdrawal_address
            }
        }

        response = requests.post(url, headers = headers, json = body)

        return response

    def create_crypto_withdrawal(self, cryptocurrency_code, cryptocurrency_blockchain_id, withdrawal_address, amount, extra_data):
        url = self.BASE + f"/transactions/withdrawals/create/"

        body = {
            "data": {
                "cryptocurrency_code": cryptocurrency_code,
                "cryptocurrency_blockchain_id": cryptocurrency_blockchain_id,
                "cryptocurrency_amount": float(amount),
                "withdrawal_address": withdrawal_address,
                "extra_data": extra_data
            }
        }
        
        response = requests.post(url, headers = self.HEADERS, json = body)

        return response

    # def is_valid_address(self, blockchain, network, address):
    #     url = self.BASE +  f"/blockchain-tools/{blockchain}/{network}/addresses/validate"
    #     data ={
    #             "context": "",
    #             "data": {
    #                 "item": {
    #                     "address": f"{address}"
    #                 }
    #             }
    #         }

    #     request = requests.post(url, headers=self.HEADERS, json=data).json()
        
    #     return request["data"]["item"]["isValid"]

    # def get_token_transaction_details_by_transactionid(self, blockchain, network, transactionHash):
    #     url = self.BASE +  f" /blockchain-data/{blockchain}/{network}/transactions/{transactionHash}/tokens-transfers"
    #     request = requests.get(url, headers=self.HEADERS).json()

    #     return request["data"]["items"]
        
        pass

        # https://api.cryptosharepay.com/v1/accounts/account-customer-id/

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

