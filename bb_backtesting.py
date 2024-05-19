import backtrader as bt
import yfinance as yf
import pandas as pd

class BollingerBandsStrategy(bt.Strategy):
    params = (
        ('period', 14),
        ('upper_bound', 2),
        ('lower_bound', 1)
    )

    def __init__(self):
        self.bollinger = bt.indicators.BollingerBands(self.data, period=self.params.period)
        self.upper_bound = self.params.upper_bound
        self.lower_bound = self.params.lower_bound

    def next(self):
        if self.data.close[0] > self.bollinger.lines.top[0]:
            # Sell when the close price crosses above the upper band
            self.sell()

        elif self.data.close[0] < self.bollinger.lines.bot[0]:
            # Buy when the close price crosses below the lower band
            self.buy()

# Load data from yfinance
data = bt.feeds.PandasData(dataname=yf.download('SPY', period='1Y', interval='1d'))

# Create a cerebro instance
cerebro = bt.Cerebro()

# Add strategy
cerebro.addstrategy(BollingerBandsStrategy)

# Add data to cerebro
cerebro.adddata(data)

# Run backtest
cerebro.run()

# Plot results
cerebro.plot(style='candlestick')
