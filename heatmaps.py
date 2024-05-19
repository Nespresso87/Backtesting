from backtesting import Backtest, Strategy
from backtesting.test import GOOG
from backtesting.lib import crossover, plot_heatmaps
import talib
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#print(GOOG)

data = yf.download('GOOGL', period='60d', interval='15m')
#data = yf.download('GOOGL', period='60d', interval='5m')
#data = yf.download('GOOGL', period='1y', interval='1d')
#data = yf.download('GOOGL', period='7d', interval='1m')
#data = yf.download('GOOGL', period='100d', interval='1H')

def optim_func(series):

    if series["# Trades"] < 10:
        return -1

    return series["Equity Final [$]"]/series["Exposure Time [%]"]

class RsiOscillator(Strategy):

    upper_bound = 70
    lower_bound = 30
    rsi_window = 14
    
    def init(self):
        self.rsi = self.I(talib.RSI,self.data.Close,self.rsi_window)

    def next(self):
        if crossover(self.rsi, self.upper_bound):
            self.position.close()

        elif crossover(self.lower_bound,self.rsi):
            self.buy()

bt = Backtest(data, RsiOscillator,cash=10000)
stats, heatmap = bt.optimize(
    upper_bound = range(10,85,5),
    lower_bound = range(10,85,5),
    rsi_window = range(10,45,5),
    maximize='Sharpe Ratio',
    constraint= lambda param: param.upper_bound > param.lower_bound,
    return_heatmap = True, max_tries = 100
    )
print(heatmap)
plot_heatmaps(heatmap,agg='mean')
#hm = heatmap.groupby(["upper_bound","lower_bound"]).mean().unstack()
#sns.heatmap(hm)
#plt.show()
#print(hm)