"""
Stock data model. Represents a single stock with its data and metadata.
"""

class Stock:
    def __init__(self, ticker):
        """
        Initialize with a ticker symbol.
        Should store: ticker, company name, historical data (DataFrame),
        and current price.
        """

    def load_history(self, start_date, end_date):
        """
        Use data_fetcher to populate this stock's historical data.
        """

    def get_latest_price(self):
        """
        Return the most recent closing price from the loaded data.
        """

    def get_price_on_date(self, date):
        """
        Return the closing price on a specific date.
        Useful for backtesting.
        """

    def summary(self):
        """
        Print/return a summary: ticker, date range loaded, latest price,
        52-week high/low, average volume.
        """
