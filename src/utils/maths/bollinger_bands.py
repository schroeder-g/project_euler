import pandas as pd
from pandas_datareader import data as pdr
import numpy as np
import datetime


"""
Appends bollinger bands to a pandas dataframe

data = a pandas dataframe or series
window = the lookback period
num_stds = how many standard deviations
"""


def bollinger_strat(data, window, num_stds):
    rolling_mean = data["Close"].rolling(window).mean()
    rolling_std = data["Close"].rolling(window).std()

    df["Bollinger High"] = rolling_mean + (rolling_std * num_stds)
    df["Bollinger Low"] = rolling_mean - (rolling_std * num_stds)


bollinger_strat(data, 20, 2)
