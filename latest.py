from backtesting import Backtest, Strategy
from backtesting.test import GOOG
from backtesting.lib import crossover
import talib
import yfinance as yf
import pandas as pd

import yfinance as yf
'''
def get_stock_data_for_date(symbol, date, period="1d", interval="1d"):
    """
    Get stock data for a particular date.
    
    Args:
    - symbol (str): Stock symbol (e.g., AAPL for Apple Inc.)
    - date (str): Date in the format 'YYYY-MM-DD'
    - period (str): Data period to download (e.g., "1d" for 1 day, "1mo" for 1 month)
    - interval (str): Data interval (e.g., "1d" for 1 day, "1wk" for 1 week)
    
    Returns:
    - pandas DataFrame: Stock data for the specified date
    """
    stock_data = yf.download(symbol, start=date, end=date, period=period, interval=interval)
    return stock_data

# Example usage:
symbol = "SPY"  # Apple Inc.
date = "2024-03-27"
period = "1d"  # 1 day
interval = "1m"  # 1 minute interval
data = get_stock_data_for_date(symbol, date, period, interval)'''
#print(stock_data)


#data = yf.download('TSLA', period='60d', interval='15m')
#data = yf.download('QQQ', period='60d', interval='15m')
#data = yf.download('SPY', period='60d', interval='5m')
data = yf.download('SPY', start="2024-05-13",end="2024-05-18", interval='5m')

#data = yf.download('GOOGL', period='1y', interval='1d')
#data = yf.download('QQQ', period='7d', interval='1m')
#data = yf.download('TSLA', period='100d', interval='1H')
#data = yf.download('GOOGL', period='60d', interval='90m')
#data = yf.download('SPY', period='2y', interval='1d')
#print(data)

def optim_func(series):

    if series["# Trades"] < 10:
        return -1

    #return series["Equity Final [$]"]/series["Exposure Time [%]"]
    return series["Sharpe Ratio"]
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
stats = bt.optimize(
    upper_bound = range(50,85,2),
    lower_bound = range(10,50,2),
    #rsi_window = range(10,30,2),
    maximize=optim_func,
    constraint= lambda param: param.upper_bound > param.lower_bound
    ,max_tries=100
    )
print(stats)
bt.plot()
