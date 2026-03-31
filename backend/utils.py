"""
Helper/utility functions used across modules.
"""

import yfinance as yf

def format_currency(amount):
    """
    Format a float as a dollar string, e.g. 1234.5 -> "$1,234.50"
    """
    s = f"${amount:,.2f}"
    return s

def format_percentage(value):
    """
    Format a float as a percentage string, e.g. 0.156 -> "15.60%"
    """
    s = f"{value:.2%}"
    return s

def validate_ticker(ticker):
    """
    Check if a ticker symbol is valid (exists and has data).
    Returns True/False.
    """
    t = yf.Ticker(ticker)
    if t.info:
        return True
    return False


def parse_date(date_string):
    """
    Parse a date string into a datetime object. Handle common formats.
    """

def print_table(headers, rows):
    """
    Pretty-print tabular data to the console (for portfolio, results, etc).
    """
    
