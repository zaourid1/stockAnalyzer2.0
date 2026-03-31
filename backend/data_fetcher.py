"""
Responsible for fetching stock data from external APIs.
Recommended library: yfinance (free, no API key needed).
"""

def fetch_stock_data(ticker, start_date, end_date):
    """
    Fetch historical OHLCV data (Open, High, Low, Close, Volume) for a given
    ticker symbol between two dates.
    Returns a pandas DataFrame with date-indexed rows.
    """

def fetch_realtime_price(ticker):
    """
    Fetch the current/latest price for a ticker.
    Returns a float.
    """

def fetch_multiple_stocks(tickers, start_date, end_date):
    """
    Fetch historical data for a list of tickers at once.
    Returns a dict of {ticker: DataFrame}.
    """

def save_data_to_csv(dataframe, filename):
    """
    Cache fetched data locally as a CSV so you don't re-fetch every time.
    """

def load_data_from_csv(filename):
    """
    Load previously cached stock data from a CSV file.
    Returns a DataFrame.
    """
