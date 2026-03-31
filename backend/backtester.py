"""
Backtesting engine. Runs a strategy against historical data to see
how it would have performed.
"""

class Backtester:
    def __init__(self, strategy, data, starting_balance=10000.0):
        """
        Takes a Strategy object, a DataFrame of historical stock data,
        and a starting balance. Creates an internal Portfolio.
        """

    def run(self):
        """
        Iterate through each day in the data. Use strategy.generate_signals()
        to get signals, then execute buys/sells on the internal portfolio.
        Track portfolio value over time.
        """

    def get_results(self):
        """
        Return a dict of performance metrics:
        - Total return (%)
        - Number of trades
        - Win rate (% of profitable trades)
        - Max drawdown (largest peak-to-trough decline)
        - Sharpe ratio (risk-adjusted return)
        - Final portfolio value
        """

    def plot_results(self):
        """
        Plot portfolio value over time vs. buy-and-hold.
        Mark buy/sell points on the stock price chart.
        Use matplotlib.
        """
