from sklearn.linear_model import LinearRegression
import numpy as np

def prepare_data(data):
    p, v = [], []
    for entry in data:
        p.append(entry[0])
        v.append(entry[1])
    return p, v

def lsm(prepared_data):
    p, v = prepared_data

    x = np.array(p).reshape(-1,1)
    y = np.array(v)

    return LinearRegression().fit(x, y)

def analyze_coef(coef):
    if abs(coef) < 0.1:
        return "Neutral" 
    elif coef < -1:
        return "Bullish"
    elif coef < 0:
        return "Slightly Bullish"
    elif coef > 1:
        return "Bearish"
    else:
        return "Slightly Bearish"