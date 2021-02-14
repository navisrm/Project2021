import functions as func
import time
import main_application as mn
import logging
import sys


def main():

    """
    variables
    """
    # ticker to read from application properties file
    # ticker = mn.ticker

    ticker = sys.argv[1]
    pnl = 0
    counter = 0
    start_price = func.get_current_price(ticker)

    """Instantiating log"""
    func.intantiate_log(ticker)

    while True:

        curr_ticker_price1 = func.get_current_price(ticker)

        if curr_ticker_price1 < start_price:
            start_price = curr_ticker_price1

        # start_price is variable. locked_price is set to latest start_price*(the value set in config file)
        locked_price = func.lock_in_price(start_price)

        logging.info("start_price: " + str(start_price) + "; " + "current_ticker_price: " + str(curr_ticker_price1) +
                     "; " + "lock_in_price: " + str(func.lock_in_price(start_price)))

        if curr_ticker_price1 > locked_price:

            # Since the locked price is set, evaluate the exit_profit_price and exit_loss_price to avoid
            # calling functions multiple times
            exit_pf_price = func.exit_profit_price(curr_ticker_price1)
            exit_ls_price = func.exit_loss_price(curr_ticker_price1)

            logging.info("Buy Order placed")
            func.prints(curr_ticker_price1, locked_price, exit_pf_price,
                        exit_ls_price, pnl, "Buy")

            while True:

                curr_ticker_price2 = func.get_current_price(ticker)

                func.prints(curr_ticker_price2, locked_price, exit_pf_price,
                            exit_ls_price, pnl, "Sell-Check")

                if curr_ticker_price2 > exit_pf_price or curr_ticker_price2 < exit_ls_price:
                    logging.info("Sell Order placed")
                    profit_loss = curr_ticker_price2 - locked_price
                    if profit_loss >= 0:
                        logging.info("Transaction is Profit: " + str(profit_loss))
                    else:
                        logging.info("Transaction is loss: " + str(profit_loss))
                    pnl += profit_loss
                    func.prints(curr_ticker_price2, locked_price, exit_pf_price,
                                exit_ls_price, pnl, "Sell")
                    break
                time.sleep(int(mn.sleep_time))

                start_price = func.get_current_price(ticker)

        time.sleep(int(mn.sleep_time))






