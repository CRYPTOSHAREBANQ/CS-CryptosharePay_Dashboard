from .cryptosharepay import CryptoSharePay
import json

class CryptoSharePayUtils:
    def __init__(self):
        self.cryptosharepay_client = CryptoSharePay()

    def request_customer_id(self, email, password):
        response = self.cryptosharepay_client.request_customer_id(email, password)

        if response.status_code != 200:
            return json.loads(response._content.decode().replace("'",'"'))
        else:
            return response.json()
