import configparser
import application_logic
import logging
import main_application as mn


config = configparser.RawConfigParser()
config.read('application.properties')


lock_price = config.get('ApplicationParams', 'lock_price')
exit_profit = config.get('ApplicationParams', 'exit_profit')
exit_loss = config.get('ApplicationParams', 'exit_loss')
sleep_time = config.get('ApplicationParams', 'sleep_time')
log_loc = config.get('ApplicationParams', 'log_location')


"""
This block contains the logging initializer.
Import logging package and use the logger object for logging
"""
LOG = mn.log_loc
logging.basicConfig(filename=LOG, filemode="w", level=logging.INFO)
# console handler
console = logging.StreamHandler()
console.setLevel(logging.ERROR)
logging.getLogger("").addHandler(console)


if __name__ == "__main__":
    application_logic.main()

