import functions as func
import time
import requests



while True:
    try:
        start_price = func.get_ticker_price("BTCUSDT")
        print(start_price)
    except requests.exceptions.ConnectTimeout:
        print("Connection TimeOut exception from Binance API")
        print(str(start_price) + " -inside except")
        continue
    except requests.exceptions.ReadTimeout:
        print("Read TimeOut exception from Binance API")
        print(str(start_price) + " -inside except")
        continue
    print("Tummy Time")
