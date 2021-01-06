import functions as func
import time
import requests

"""
variables
"""
ticker = "ETHUSDT"
pnl = 0


while True:
    try:
        start_price = func.get_ticker_price(ticker)
    except requests.exceptions.ConnectTimeout:
        print("Connection TimeOut exception from Binance API")
        continue
    except requests.exceptions.ReadTimeout:
        print("Read TimeOut exception from Binance API")
        continue
    break


while True:

    while True:
        try:
            curr_ticker_price1 = func.get_ticker_price(ticker)
        except requests.exceptions.ConnectTimeout:
            print(str(curr_ticker_price1) + " -Connection TimeOut exception from Binance API")
            continue
        except requests.exceptions.ReadTimeout:
            print(str(curr_ticker_price1) + " -Read TimeOut exception from Binance API")
            continue
        break

    if curr_ticker_price1 < start_price:
        start_price = curr_ticker_price1

    # start_price is variable. locked_price is set to latest start_price*(the value set in config file)

    locked_price = func.lock_in_price(start_price)

    print("start_price: " + str(start_price) + "; " + "current_ticker_price: " + str(curr_ticker_price1) + "; " +
          "lock_in_price: " + str(func.lock_in_price(start_price)))

    if curr_ticker_price1 > locked_price:

        # Since the locked price is set, evaluate the exit_profit_price and exit_loss_price to avoid
        # calling functions multiple times
        exit_pf_price = func.exit_profit_price(locked_price)
        exit_ls_price = func.exit_loss_price(locked_price)

        print("ticker price is more than 1% of start price. Buy Order placed")
        func.prints(curr_ticker_price1, locked_price, exit_pf_price,
                    exit_ls_price, pnl, "Buy")

        while True:

            while True:
                try:
                    curr_ticker_price2 = func.get_ticker_price(ticker)
                except requests.exceptions.ConnectTimeout:
                    print(str(curr_ticker_price1) + " -Connection TimeOut exception from Binance API")
                    continue
                except requests.exceptions.ReadTimeout:
                    print(str(curr_ticker_price1) + " -Read TimeOut exception from Binance API")
                    continue
                break

            func.prints(curr_ticker_price2, locked_price, exit_pf_price,
                        exit_ls_price, pnl, "Sell-Check")

            if curr_ticker_price2 > exit_pf_price or curr_ticker_price2 < exit_ls_price:
                print("Sell Order placed")
                profit_loss = curr_ticker_price2 - locked_price
                pnl += profit_loss
                func.prints(curr_ticker_price1, locked_price, exit_pf_price,
                            exit_ls_price, pnl, "Sell")
                break
            time.sleep(5)

            while True:
                try:
                    start_price = func.get_ticker_price(ticker)
                except requests.exceptions.ConnectTimeout:
                    print(str(curr_ticker_price1) + " -Connection TimeOut exception from Binance API")
                    continue
                except requests.exceptions.ReadTimeout:
                    print(str(curr_ticker_price1) + " -Read TimeOut exception from Binance API")
                    continue
                break

    time.sleep(5)






