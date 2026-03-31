"""
Tracks your paper trading portfolio: cash balance, stock holdings,
and transaction history.
"""

class Portfolio:
    def __init__(self, starting_balance=10000.0):
        """
        Initialize with a cash balance. Holdings should be a dict
        {ticker: num_shares}. Keep a list of all transactions.
        """

    def buy(self, ticker, price, quantity):
        """
        Execute a buy: deduct cash, add shares to holdings,
        log the transaction. Should check if you have enough cash.
        """

    def sell(self, ticker, price, quantity):
        """
        Execute a sell: add cash, remove shares from holdings,
        log the transaction. Should check if you own enough shares.
        """

    def get_total_value(self, current_prices):
        """
        Calculate total portfolio value: cash + (shares * current price)
        for each holding. current_prices is a dict {ticker: price}.
        """

    def get_profit_loss(self, current_prices):
        """
        Total P&L = current total value - starting balance.
        Returns dollar amount and percentage.
        """

    def get_holdings(self):
        """
        Return a summary of current holdings: ticker, shares, avg cost.
        """

    def get_transaction_history(self):
        """
        Return the full list of all buy/sell transactions with dates,
        prices, and quantities.
        """

    def save_to_file(self, filepath):
        """
        Persist portfolio state to a JSON file so you can resume later.
        """

    def load_from_file(self, filepath):
        """
        Restore portfolio state from a saved JSON file.
        """
