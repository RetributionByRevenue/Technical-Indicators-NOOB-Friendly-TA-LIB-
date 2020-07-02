import krakenex
from pykrakenapi import KrakenAPI
api = krakenex.API()
k = KrakenAPI(api)
ohlc, last = k.get_ohlc_data(pair="BCHUSD", interval=30)
print('Fetching from Kraken API:\n',ohlc.head(1),'\n')

import numpy as np
import talib

close = np.array(ohlc.close.to_list())
high = np.array(ohlc.high.to_list())
low = np.array(ohlc.low.to_list())
print("Candlestick information:")
print("Candle Close\n",close[-10:],"\n")
print("Candle High\n",high[-10:],"\n")
print("Candle Low\n",low[-10:],"\n")

simple_moving_average=talib.SMA(close)
print("simple_moving_average:\n",simple_moving_average[-10:],"\n")

macd, macdsignal, macdhist = talib.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
print("MACD:\n",macd[-10:],"\n")

parbolic_sar = talib.SAR(high, low, acceleration=1, maximum=1)
print("parbolic_sar:\n",parbolic_sar[-10:],"\n")
