import json
STORAGE_DIR = "/home/volodymyrsemko/work/uni_practice/danTV/storage/"

def fread(filename):
    f = open(f"{STORAGE_DIR}{filename}")

    data = json.load(f)

    prep_data = [[(entry["price_open"] + entry["price_close"])/2, entry["volume_traded"]] for entry in data]
    ref = prep_data[0]
    bars = prep_data[1:]
    return {"REF": ref, "BARS": bars}
        