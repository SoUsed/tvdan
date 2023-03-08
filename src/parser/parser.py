import requests
from datetime import datetime, timedelta
from parser.cred_reader import get_credentials
import sys
STORAGE_DIR = "/home/volodymyrsemko/work/uni_practice/danTV/storage/"

class ParserConfig:
    tickerid: str
    timeframe: str
    lookback: int

    def __init__(self, tickerid, timeframe, lookback = 0):
        self.tickerid = tickerid
        self.timeframe = timeframe
        self.lookback = lookback

DEFAULT_PARSER_CONFIG = ParserConfig("BITSTAMP_SPOT_BTC_USD", "30MIN")

class ParserTV:
    def process(self, config):
        iso_date_now = datetime.now().isoformat()
        iso_date_yesterday = (datetime.now() - timedelta(1 + config.lookback)).strftime('%Y-%m-%d') + "T23:30:00"

        url = f'https://rest.coinapi.io/v1/ohlcv/{config.tickerid}/history?period_id={config.timeframe}&time_start={iso_date_yesterday}'
        print(url)

        if config.lookback:
            iso_date_end = (datetime.now() - timedelta(config.lookback)).strftime('%Y-%m-%d') + "T23:59:59"
            url += f'&time_end={iso_date_end}'

        headers = self.credentials
        response = requests.get(url, headers=headers)
        fname = f"{config.tickerid}{config.timeframe}{iso_date_now}.json"

        original_stdout = sys.stdout
        with open(f"{STORAGE_DIR}{fname}", 'w') as f:
            sys.stdout = f # Change the standard output to the file we created.
            print(str(response.json()).replace("'", '"'))
            sys.stdout = original_stdout # Reset the standard output to its original value

        return fname

    def __init__(self):
        self.credentials = get_credentials()

if __name__ == '__main__':
    parser = ParserTV(DEFAULT_PARSER_CONFIG)
    parser.process()
