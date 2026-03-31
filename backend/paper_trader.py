"""
Paper trading simulator. Like backtesting but uses current/live data
and runs in a forward-looking manner.
"""

class PaperTrader:
    def __init__(self, strategy, tickers, starting_balance=10000.0):
        """
        Initialize with a strategy, list of tickers to watch,
        and a portfolio with the starting balance.
        """

    def execute_cycle(self):
        """
        One trading cycle: fetch latest prices, run strategy signals,
        execute any trades on the portfolio. Call this manually or on
        a schedule.
        """

    def get_status(self):
        """
        Return current portfolio state: holdings, cash, total value, P&L.
        """

    def save_state(self):
        """
        Save the current paper trading session to disk so you can
        resume later.
        """

    def load_state(self):
        """
        Resume a previous paper trading session from disk.
        """
