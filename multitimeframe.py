from backtesting import Backtest, Strategy
from backtesting.test import GOOG
from backtesting.lib import crossover, resample_apply
import talib
import yfinance as yf
import pandas as pd
#print(GOOG)

#data = yf.download('GOOGL', period='60d', interval='15m')
#data = yf.download('GOOGL', period='60d', interval='5m')
#data = yf.download('GOOGL', period='1y', interval='1d')
#data = yf.download('GOOGL', period='7d', interval='1m')
#data = yf.download('GOOGL', period='100d', interval='1H')
#data = yf.download('GOOGL', period='60d', interval='90m')
#data = yf.download('GOOGL', period='60d', interval='15m')
data = yf.download('GOOGL',period='2y',interval='1d')

def optim_func(series):

    if series["# Trades"] < 10:
        return -1

    return series["Equity Final [$]"]/series["Exposure Time [%]"]

class RsiOscillator(Strategy):

    upper_bound = 70
    lower_bound = 30
    rsi_window = 14
    
    def init(self):
        self.daily_rsi = self.I(talib.RSI,self.data.Close,self.rsi_window)
        self.weekly_rsi = resample_apply(
        "H", talib.RSI, self.data.Close, self.rsi_window)
    def next(self):
        if (crossover(self.daily_rsi, self.upper_bound)
            and self.weekly_rsi[-1] > self.upper_bound):
            self.position.close()

        elif (crossover(self.lower_bound,self.daily_rsi)
            and self.weekly_rsi[-1] < self.lower_bound
            and self.daily_rsi[-2] < self.weekly_rsi[-1]):
            self.buy()

bt = Backtest(data, RsiOscillator,cash=10000)
'''stats = bt.optimize(
    upper_bound = range(50,85,2),
    lower_bound = range(10,50,2),
    rsi_window = range(10,30,2),
    maximize='Sharpe Ratio',
    constraint= lambda param: param.upper_bound > param.lower_bound
    ,max_tries=100
    )'''
stats= bt.run()
bt.plot()
print(stats)
