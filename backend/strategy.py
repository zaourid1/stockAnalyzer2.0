"""
Trading strategy definitions. Each strategy is a class that takes
stock data + indicators and produces BUY/SELL/HOLD signals.
"""

class Strategy:
    def __init__(self, name):
        """
        Base strategy class. Store the strategy name and any parameters.
        """

    def generate_signals(self, data):
        """
        Given a DataFrame of stock data, return a Series of signals:
        1 = BUY, -1 = SELL, 0 = HOLD for each date.
        This is the method subclasses must override.
        """


class SMACrossover(Strategy):
    def __init__(self, short_window=20, long_window=50):
        """
        Buy when short SMA crosses above long SMA.
        Sell when short SMA crosses below long SMA.
        """

    def generate_signals(self, data):
        """
        Compute short & long SMAs, detect crossovers,
        return signal Series.
        """


class RSIStrategy(Strategy):
    def __init__(self, oversold=30, overbought=70):
        """
        Buy when RSI drops below oversold threshold.
        Sell when RSI rises above overbought threshold.
        """

    def generate_signals(self, data):
        """
        Compute RSI, compare to thresholds, return signal Series.
        """


class MACDStrategy(Strategy):
    def __init__(self):
        """
        Buy when MACD line crosses above signal line.
        Sell when MACD line crosses below signal line.
        """

    def generate_signals(self, data):
        """
        Compute MACD, detect crossovers, return signal Series.
        """
