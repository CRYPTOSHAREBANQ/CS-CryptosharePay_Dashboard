from .cryptosharepay import CryptoSharePay
import json

class CryptoSharePayUtils:
    def __init__(self, api_key = None):
        self.cryptosharepay_client = CryptoSharePay(
            api_key = api_key
            )

    def post_process_request(self, response):
        if response.status_code != 200:
            return json.loads(response._content.decode().replace("'",'"'))
        else:
            return response.json()

    def get_account_customer_id(self, email, password, security_pin):
        response = self.cryptosharepay_client.get_account_customer_id(email, password, security_pin)

        post_response = self.post_process_request(response)

        return post_response

    def get_digital_currencies(self):
        response = self.cryptosharepay_client.get_digital_currencies()

        post_response = self.post_process_request(response)

        return post_response

    def get_cryptocurrencies(self):
        response = self.cryptosharepay_client.get_cryptocurrencies()

        post_response = self.post_process_request(response)

        return post_response

    def request_account_customer_id(self, email, password):
        response = self.cryptosharepay_client.request_account_customer_id(email, password)

        post_response = self.post_process_request(response)

        return post_response

    def create_digital_transaction_digital_to_crypto(self, description, digital_currency_code, digital_currency_amount, cryptocurrency_code, cryptocurrency_blockchain_id):
        response = self.cryptosharepay_client.create_digital_transaction_digital_to_crypto(description, digital_currency_code, digital_currency_amount, cryptocurrency_code, cryptocurrency_blockchain_id)

        post_response = self.post_process_request(response)

        return post_response