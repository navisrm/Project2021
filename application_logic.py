import functions as func
import time
import main_application as mn
import logging
import sys
from datetime import datetime


def main():

    """variables"""
    ticker = sys.argv[1]
    pnl = 0
    counter = 0
    start_price = func.get_current_price(ticker)

    """Instantiating log"""
    func.intantiate_log(ticker)

    try:
        while True:

            curr_ticker_price1 = func.get_current_price(ticker)

            if curr_ticker_price1 < start_price:
                start_price = curr_ticker_price1

            # start_price is variable. locked_price is set to latest start_price*(the value set in config file)
            locked_price = func.lock_in_price(start_price)

            if curr_ticker_price1 > locked_price:

                # Since the locked price is set, evaluate the exit_profit_price and exit_loss_price to avoid
                # calling functions multiple times
                exit_pf_price = func.exit_profit_price(curr_ticker_price1)
                exit_ls_price = func.exit_loss_price(curr_ticker_price1)

                logging.info("Buy Order placed" + " - " + "current ticker price: " + str(curr_ticker_price1) +
                             ", locked ticker price: " + str(locked_price) + ", exit profit set: " + str(exit_pf_price) +
                             ", exit loss set: " + str(exit_ls_price))

                try:
                    while True:

                        curr_ticker_price2 = func.get_current_price(ticker)

                        if curr_ticker_price2 > exit_pf_price or curr_ticker_price2 < exit_ls_price:

                            profit_loss = curr_ticker_price2 - locked_price

                            if profit_loss >= 0:
                                logging.info("Transaction is Profit: " + str(profit_loss))
                            else:
                                logging.info("Transaction is loss: " + str(profit_loss))
                            pnl += profit_loss

                            logging.info("Sell Order placed" + " - " + "Bought Price: " + str(curr_ticker_price1) +
                                         ", Sold Price: " + str(curr_ticker_price2)
                                         + ", Current P/L: " + str(profit_loss) + ", PNL: " + str(pnl))

                            break
                        time.sleep(int(mn.sleep_time))

                        # The code below increments the counter and logs the price details.
                        # It helps in minimizing the log details
                        counter += 1
                        if counter == 6:
                            counter = 0
                            logging.info(str(datetime.now()) + " - " + "Transactional Block - " +
                                         "current_ticker_price: " + str(curr_ticker_price2) +
                                         "; " + "Bought Price: " + str(curr_ticker_price1) + ", exit profit set: " +
                                         str(exit_pf_price) + ", exit loss set: " + str(exit_ls_price))

                        # Initialize the start_price variable after transaction is completed
                        start_price = func.get_current_price(ticker)

                except BaseException as e:
                    logging.ERROR("ERROR: " + str(e))
                    sys.exit()

            time.sleep(int(mn.sleep_time))

            # The code below increments the counter and logs the price details.
            # It helps in minimizing the log details
            counter += 1
            if counter == 6:
                counter = 0
                logging.info(str(datetime.now()) + " - " +
                             "current_ticker_price: " + str(curr_ticker_price1) +
                             "; " + "locked_price: " + str(func.lock_in_price(start_price)))

    except BaseException as e:
        logging.ERROR("ERROR: " + str(e))
        sys.exit()




