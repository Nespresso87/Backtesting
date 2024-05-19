RSI Oscillator Strategy
This repository contains a trading strategy implemented using the Backtrader library, designed to trade the SPY based on the Relative Strength Index (RSI) oscillator. The strategy aims to capitalize on overbought and oversold market conditions identified by the RSI indicator.

Strategy Overview
The RSI Oscillator strategy leverages both daily and hourly RSI indicators to make trading decisions. The key components of the strategy are:

Daily RSI: Calculated using the closing prices with a window period of 14 days.
Hourly RSI: Resampled from the daily closing prices to calculate the RSI with a window period of 14 hours.
Trading Logic
Sell Signal: A sell signal is triggered when the daily RSI crosses above the upper bound (70), indicating overbought conditions, and the hourly RSI is also above the upper bound.
Buy Signal: A buy signal is triggered when the daily RSI crosses below the lower bound (30), indicating oversold conditions, and the hourly RSI is also below the lower bound, with the daily RSI being lower than the hourly RSI in the previous period.
Optimization
The strategy includes an optimization function to maximize the final equity relative to the exposure time, provided the number of trades is greater than 10. Parameters such as the upper and lower bounds and the RSI window period can be optimized to achieve better performance.
