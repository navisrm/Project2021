import configparser
import application_logic

config = configparser.RawConfigParser()
config.read('application.properties')

lock_price = config.get('ApplicationParams', 'lock_price')
exit_profit = config.get('ApplicationParams', 'exit_profit')
exit_loss = config.get('ApplicationParams', 'exit_loss')
sleep_time = config.get('ApplicationParams', 'sleep_time')


if __name__ == "__main__":
    application_logic.main()

