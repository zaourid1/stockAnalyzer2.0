"""
Technical analysis functions. Each takes a DataFrame of stock data
and returns the computed indicator as a Series or value.
"""

def calculate_sma(data, window):
    """
    Simple Moving Average over a given window (e.g. 20, 50, 200 days).
    Returns a pandas Series.
    """

def calculate_ema(data, window):
    """
    Exponential Moving Average — weights recent prices more heavily.
    Returns a pandas Series.
    """

def calculate_rsi(data, period=14):
    """
    Relative Strength Index — momentum oscillator (0-100).
    Above 70 = overbought, below 30 = oversold.
    Returns a pandas Series.
    """

def calculate_macd(data, fast=12, slow=26, signal=9):
    """
    Moving Average Convergence Divergence.
    Returns a tuple: (macd_line, signal_line, histogram) — all Series.
    """

def calculate_bollinger_bands(data, window=20, num_std=2):
    """
    Bollinger Bands — upper, middle (SMA), and lower bands.
    Returns a tuple: (upper_band, middle_band, lower_band).
    """

def calculate_daily_returns(data):
    """
    Percentage change day-over-day.
    Returns a pandas Series.
    """

def calculate_volatility(data, window=30):
    """
    Rolling standard deviation of daily returns.
    Higher = riskier stock. Returns a pandas Series.
    """
