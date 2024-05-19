from datetime import datetime
import backtrader as bt
import yfinance as yf

class SmaCross(bt.SignalStrategy):
    def __init__(self):
        sma1, sma2 = bt.ind.SMA(period=50), bt.ind.SMA(period=200)
        crossover = bt.ind.CrossOver(sma1, sma2)
        self.signal_add(bt.SIGNAL_LONG, crossover)

# Create a cerebro instance
cerebro = bt.Cerebro()

# Add strategy
cerebro.addstrategy(SmaCross)

# Load data from yfinance
data = bt.feeds.PandasData(dataname=yf.download('GOOGL', start='2023-01-01', end='2024-03-24'))

# Add data to cerebro
cerebro.adddata(data)

# Run backtest
cerebro.run()

# Plot results
cerebro.plot()
