from datetime import datetime
import backtrader as bt
import yfinance as yf

class BollingerBandsStrategy(bt.Strategy):
    params = (
        ('period', 20),
        ('devfactor', 2),
    )

    def __init__(self):
        self.bollinger = bt.indicators.BollingerBands(self.data, period=self.params.period, devfactor=self.params.devfactor)

    def next(self):
        if self.data.close[0] < self.bollinger.lines.bot[0]:
            # Buy when the close price crosses below the lower band
            self.buy()
        elif self.data.close[0] > self.bollinger.lines.top[0]:
            # Sell when the close price crosses above the upper band
            self.sell()

# Create a cerebro instance
cerebro = bt.Cerebro()

# Add strategy
cerebro.addstrategy(BollingerBandsStrategy)

# Load data from yfinance
data = bt.feeds.PandasData(dataname=yf.download('SPY', start='2023-01-01', end='2024-03-24'))

# Add data to cerebro
cerebro.adddata(data)

# Run backtest
cerebro.run()

# Plot results
cerebro.plot()
