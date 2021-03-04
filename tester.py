from binance.client import Client
import json
from binance.enums import *

# Access Tokens - The required tokens are imported in the below block
with open('credentials.json') \
        as data_file:
    data = json.load(data_file)
    api_key = data["api_key"]
    secret_key = data["secret_key"]
    twilio_account_sid = data["twilio_account_sid"]
    twilio_auth_token = data["twilio_auth_token"]


# client = Client(api_key, secret_key)
client = Client(api_key, secret_key)

orders = client.get_all_orders()
print(orders)

"""
order = client.order_limit_buy(
    symbol='ADABTC',
    quantity=10,
    price='0.00001429')

print(order)

order_status = client.get_order(
    symbol='ADABTC',
    orderId='286138401')
print(order_status)
"""

