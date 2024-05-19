import backtrader as bt
import pandas as pd
import yfinance as yf
class BollingerBandsStrategy(bt.Strategy):
    params = (
        ("period", 20),
        ("devfactor", 2),
    )

    def __init__(self):
        self.bollinger = bt.indicators.BollingerBands(self.data, period=self.params.period, devfactor=self.params.devfactor)

    def next(self):
        if self.data.close > self.bollinger.lines.top:
            self.sell()
        elif self.data.close < self.bollinger.lines.bot:
            self.buy()

# Load data
data = yf.download('SPY',period='1y',interval='1d')

# Initialize backtest
cerebro = bt.Cerebro()
cerebro.adddata(data)
cerebro.addstrategy(BollingerBandsStrategy)

# Set starting cash
cerebro.broker.setcash(100000)

# Set commission - 0.1% ... divide by 100 to remove the %
cerebro.broker.setcommission(commission=0.001)

# Run backtest
cerebro.run()

# Print final portfolio value
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
