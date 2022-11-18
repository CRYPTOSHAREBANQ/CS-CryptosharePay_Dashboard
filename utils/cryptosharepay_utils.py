from .cryptosharepay import CryptoSharePay
import json

class CryptoSharePayUtils:
    def __init__(self):
        self.cryptosharepay_client = CryptoSharePay()

    def post_process_request(self, response):
        if response.status_code != 200:
            return json.loads(response._content.decode().replace("'",'"'))
        else:
            return response.json()

    def request_account_customer_id(self, email, password):
        response = self.cryptosharepay_client.request_account_customer_id(email, password)

        post_response = self.post_process_request(response)

        return post_response
    
    def get_account_customer_id(self, email, password, security_pin):
        response = self.cryptosharepay_client.get_account_customer_id(email, password, security_pin)

        post_response = self.post_process_request(response)

        return post_response