CREDENTIALS_STORAGE = r"credentials.cfg"
CONFIG_DIR = "/home/volodymyrsemko/work/uni_practice/danTV/config/"

def get_credentials() -> dict:
    """Parses TradingView credentials from the configuration files"""
    with open(f"{CONFIG_DIR}{CREDENTIALS_STORAGE}") as f:
        raw = f.read().splitlines()

        assert len(raw) == 1

        return {"X-CoinAPI-Key": raw[0]}

if __name__ == '__main__':
    print(get_credentials())
