import numpy as np
import yfinance as yf

def calculate_sharpe_ratio(returns, risk_free_rate):
    """
    Calculate Sharpe Ratio.

    Args:
    returns (array-like): Array-like object containing the historical returns of the stock.
    risk_free_rate (float): The annual risk-free rate.

    Returns:
    float: The Sharpe Ratio.
    """
    average_return = np.mean(returns)
    std_deviation = np.std(returns)
    sharpe_ratio = (average_return - risk_free_rate) / std_deviation

    return sharpe_ratio

def download_stock_returns(ticker, start_date, end_date):
    """
    Download historical stock returns data.

    Args:
    ticker (str): Stock ticker symbol.
    start_date (str): Start date for historical data in 'YYYY-MM-DD' format.
    end_date (str): End date for historical data in 'YYYY-MM-DD' format.

    Returns:
    array-like: Array-like object containing the historical returns of the stock.
    """
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    stock_returns = stock_data['Adj Close'].pct_change().dropna()

    return stock_returns

# Example usage:
ticker_symbol = 'MSFT'
start_date = '2023-01-01'
end_date = '2024-03-11'

# Download historical stock returns
stock_returns = download_stock_returns(ticker_symbol, start_date, end_date)
print(stock_returns)
# Risk-free rate, for example, let's assume 2%
risk_free_rate = 0.02

# Calculate Sharpe Ratio
sharpe_ratio = calculate_sharpe_ratio(stock_returns, risk_free_rate)
print("Sharpe Ratio:", sharpe_ratio)
