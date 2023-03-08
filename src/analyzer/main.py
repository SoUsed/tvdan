from analyzer.normalize import normalize
from analyzer.reader import fread
from analyzer.visualize import drawplot
from analyzer.regression import prepare_data, lsm

DEFAULT_FNAME = r"BITSTAMP_SPOT_BTC_USD30MIN2023-03-07T01:20:01.438277.json"

def main():
    data = fread(DEFAULT_FNAME)
    normalized_data = normalize(data["REF"], data["BARS"])
    prepared_data = prepare_data(normalized_data)
    lsm_out = lsm(prepared_data)
    drawplot(prepared_data, lsm_out)

if __name__ == '__main__':
    main()