from .cryptosharepay import CryptoSharePay
import json

class CryptoSharePayUtils:
    def __init__(self, api_key = None):
        self.cryptosharepay_client = CryptoSharePay(
            api_key = api_key
            )

    def post_process_request(self, response):
        if response.status_code != 200:
            # print(response._content.decode())
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

    def get_blockchains(self):
        response = self.cryptosharepay_client.get_blockchains()

        post_response = self.post_process_request(response)

        return post_response

    def get_businesses(self, email, customer_id):
        response = self.cryptosharepay_client.get_businesses(email, customer_id)

        post_response = self.post_process_request(response)

        return post_response

    def get_assets(self):
        response = self.cryptosharepay_client.get_assets()

        post_response = self.post_process_request(response)

        return post_response

    def request_account_customer_id(self, email, password):
        response = self.cryptosharepay_client.request_account_customer_id(email, password)

        post_response = self.post_process_request(response)

        return post_response

    def request_login_dashboard(self, email):
        response = self.cryptosharepay_client.request_login_dashboard(email)

        post_response = self.post_process_request(response)

        return post_response
    
    
    def request_individual_login_dashboard(self, email):
        response = self.cryptosharepay_client.request_individual_login_dashboard_(email)

        post_response = self.post_process_request(response)

        return post_response

    def login_dashboard(self, email, security_password):
        print('TEST1')
        response = self.cryptosharepay_client.login_dashboard(email, security_password)

        post_response = self.post_process_request(response)

        return post_response
    
    
    def login_dashboard_individual(self, email, security_password):
        print('inside Test1')
        response = self.cryptosharepay_client.Individual_login_dashboard(email, security_password)

        post_response = self.post_process_request(response)

        return post_response

    def get_api_key_by_business_id(self, customer_id, email, business_id):
        response = self.cryptosharepay_client.get_api_key_by_business_id(customer_id, email, business_id)

        post_response = self.post_process_request(response)

        return post_response
    
    
    def get_api_key_by_user_id(self, customer_id, email):
        response = self.cryptosharepay_client.get_api_key_by_user_id(customer_id, email)

        post_response = self.post_process_request(response)

        return post_response

    def get_all_payment_transactions(self):
        response = self.cryptosharepay_client.get_all_payment_transactions()

        post_response = self.post_process_request(response)

        return post_response
    
    def get_payment_transaction(self, transaction_id):
        response = self.cryptosharepay_client.get_payment_transaction(transaction_id)

        post_response = self.post_process_request(response)

        return post_response

    def create_digital_transaction_digital_to_crypto(self, description, digital_currency_code, digital_currency_amount, cryptocurrency_code, cryptocurrency_blockchain_id, withdrawal_address):
        response = self.cryptosharepay_client.create_digital_transaction_digital_to_crypto(description, digital_currency_code, digital_currency_amount, cryptocurrency_code, cryptocurrency_blockchain_id, withdrawal_address)

        post_response = self.post_process_request(response)

        return post_response

    def create_transaction_crypto_withdrawal(self, cryptocurrency_code, cryptocurrency_blockchain_id, withdrawal_address, amount, extra_data = None):
        response = self.cryptosharepay_client.create_crypto_withdrawal(cryptocurrency_code, cryptocurrency_blockchain_id, withdrawal_address, amount, extra_data)

        post_response = self.post_process_request(response)

        return post_response

    def create_account_business(self, email, password, confirm_password, first_name, last_name, country_id, birthdate, business_name, business_description):
        response = self.cryptosharepay_client.create_account(email, password, confirm_password, first_name, last_name, "TEST", country_id, birthdate, business_name, business_description)

        post_response = self.post_process_request(response)

        return post_response
    
    
    
    
    def create_indivisual_user(self,name , email, phone,country,cedula,birthdate,identity,password):
        response = self.cryptosharepay_client.create_individual_account(name , email, phone,country,cedula,birthdate,identity,password)

        post_response = self.post_process_request(response)

        return post_response