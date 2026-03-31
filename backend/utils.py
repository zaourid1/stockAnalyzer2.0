"""
Helper/utility functions used across modules.
"""

def format_currency(amount):
    """
    Format a float as a dollar string, e.g. 1234.5 -> "$1,234.50"
    """

def format_percentage(value):
    """
    Format a float as a percentage string, e.g. 0.156 -> "15.60%"
    """

def validate_ticker(ticker):
    """
    Check if a ticker symbol is valid (exists and has data).
    Returns True/False.
    """

def parse_date(date_string):
    """
    Parse a date string into a datetime object. Handle common formats.
    """

def print_table(headers, rows):
    """
    Pretty-print tabular data to the console (for portfolio, results, etc).
    """
