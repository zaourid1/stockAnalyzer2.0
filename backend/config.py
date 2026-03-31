"""
Configuration and constants for the stock analyzer.
API keys, default settings, file paths.

Ideally import API from .env file to not have API key leaked but since using
YFinance, no need for API
"""


API_KEY = ""           # Your API key (e.g. Alpha Vantage, yfinance doesn't need one)
DEFAULT_STARTING_BALANCE = 10000.00
DATA_DIR = "data/"
DATE_FORMAT = "%Y-%m-%d"
