import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from configs import TIMEFRAMES, TICKERIDS, get_request_id, CONFIG_DIR, STORAGE_DIR
from parser.parser import ParserTV, ParserConfig
from analyzer.reader import fread
from analyzer.normalize import normalize
from analyzer.regression import prepare_data, lsm, analyze_coef
from analyzer.visualize import drawplot

root = tk.Tk()
root.title("DanTV")

# prepare the configuration
ttk.Label(root, text = "Ticker").pack()
combo_box_tickerid = ttk.Combobox(root, width=50, values = TICKERIDS)
combo_box_tickerid.current(0)
combo_box_tickerid.pack()

ttk.Label(root, text = "Timeframe").pack()
combo_box_timeframe = ttk.Combobox(root, width=50, values = TIMEFRAMES)
combo_box_timeframe.current(9)
combo_box_timeframe.pack()

ttk.Label(root, text = "Lookback").pack()
lookback_entry = ttk.Spinbox(root, width=50, from_ = 0, to = 100, increment = 1)
lookback_entry.set("0")
lookback_entry.pack()

# prepare the plot
def prepare_plot():
    errmsg = ""
    # Check all of the input data
    if combo_box_tickerid.get() not in TICKERIDS:
        errmsg += "ERR | Wrong ticker specified!\n"
    if combo_box_timeframe.get() not in TIMEFRAMES:
        errmsg += "ERR | Wrong timeframe specified!\n"
    if int(lookback_entry.get()) < 0:
        errmsg += "ERR | Wrong lookback specified!\n"

    if errmsg:
        tk.messagebox.showerror("Input Error!", errmsg)
        return

    cfg = ParserConfig(get_request_id(combo_box_tickerid.get()), combo_box_timeframe.get())
    parser = ParserTV()
    filename = parser.process(cfg)
    data = fread(filename)
    normalized_data = normalize(data["REF"], data["BARS"])
    prepared_data = prepare_data(normalized_data)
    lsm_out = lsm(prepared_data)
    figure = plt.figure("DanTV")
    ax1 = figure.add_subplot()
    bar1 = FigureCanvasTkAgg(figure, root)
    bar1.get_tk_widget().pack()
    ax1.set_title("Normalized Scatter Plot")

    coef = drawplot(prepared_data, lsm_out)
    # plt.show()
    summary = f"Summary: {analyze_coef(coef)}"
    ttk.Label(root, text = summary, background="yellow").pack(side = tk.TOP, anchor = tk.NW)


calc_button = ttk.Button(root, width=50, text="Run the analysis", command = prepare_plot)
calc_button.pack()

root.mainloop()