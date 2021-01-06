from binance.client import Client
import json

"""
The functions required are listed here.
"""

# Access Tokens - The required tokens are imported in the below block
with open('C:/Users/nchennam/Desktop/Naveen/IntelliJ_Projects/TimesSquare/TimesSquare/resources/credentials.json') \
        as data_file:
    data = json.load(data_file)
    api_key = data["api_key"]
    secret_key= data["secret_key"]

# client = Client(api_key, secret_key)
client = Client(api_key, secret_key,{"timeout": 0.5})


# Get the ticker price
def get_ticker_price(symbol):
    return float(list(filter(lambda x: (x['symbol']=="ETHUSDT"),client.get_all_tickers()))[0]['price'])


# Print function
def prints(current_ticker_price, lock_price, exit_profit_pr, exit_loss_pr, pnl, order_type):
    print("curr_price:" + str(current_ticker_price) + "; " + "lock_in_price:"+ str(lock_price) + "; "
          + "exit_profit_price:" + str(exit_profit_pr) + "; " + "exit_loss_price:" + str(exit_loss_pr) + "; "
          + "pnl:" + str(pnl) + "; " + "Order_type:" + str(order_type))


# lock_in_price
def lock_in_price(price):
    return float(price*1.01)


# exit_profit_price
def exit_profit_price(price):
    return float(price*1.005)


# exit_loss_price
def exit_loss_price(price):
    return float(price*0.99)

