from binance.client import Client
from twilio.rest import Client as Client_Twilio
import json
import requests
import main_application as mn

"""
The functions required are listed here.
"""

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


def send_message(text):
    twilio_client = Client_Twilio(twilio_account_sid,twilio_auth_token)
    message = twilio_client.messages.create(
        to="+12017439933",
        from_="+16672443754",
        body=text)


# Get the ticker price
def get_ticker_price(symbol):
    return float(list(filter(lambda x: (x['symbol']==symbol),client.get_all_tickers()))[0]['price'])


# Print function
def prints(current_ticker_price, lock_price, exit_profit_pr, exit_loss_pr, pnl, order_type):
    print("curr_price:" + str(current_ticker_price) + "; " + "lock_in_price:"+ str(lock_price) + "; "
          + "exit_profit_price:" + str(exit_profit_pr) + "; " + "exit_loss_price:" + str(exit_loss_pr) + "; "
          + "pnl:" + str(pnl) + "; " + "Order_type:" + str(order_type))


# lock_in_price
def lock_in_price(price):
    return float(price*profit_num_percent_conversion(mn.lock_price))


# exit_profit_price
def exit_profit_price(price):
    return float(price*profit_num_percent_conversion(mn.exit_profit))


# exit_loss_price
def exit_loss_price(price):
    return float(price*loss_num_percent_conversion(mn.exit_loss))


# convert num to percentage for using in profits
def profit_num_percent_conversion(x):
    return (100+float(x))/100


# convert num to percentage for using in losses
def loss_num_percent_conversion(x):
    return (100-float(x))/100


# Get the current price of ticker
def get_current_price(ticker):
    while True:
        try:
            return get_ticker_price(ticker)
        except requests.exceptions.ConnectTimeout:
            print("Connection TimeOut exception from Binance API")
            continue
        except requests.exceptions.ReadTimeout:
            print("Read TimeOut exception from Binance API")
            continue
        break


