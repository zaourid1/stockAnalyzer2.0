"""
Entry point for the stock analyzer. Runs the CLI menu loop.
"""

def display_menu():
    """
    Show the main menu options to the user:
    1. Look up a stock
    2. Analyze a stock (show indicators)
    3. Backtest a strategy
    4. Start paper trading
    5. View portfolio
    6. Exit
    """

def handle_stock_lookup():
    """
    Prompt for a ticker, fetch data, display the stock summary.
    """

def handle_analysis():
    """
    Prompt for a ticker, fetch data, let user pick which indicators
    to calculate (SMA, RSI, MACD, etc.), display results.
    """

def handle_backtest():
    """
    Prompt for: ticker, date range, strategy choice, and parameters.
    Run the backtester, display results.
    """

def handle_paper_trading():
    """
    Prompt for: tickers, strategy. Start a paper trading session.
    Let user manually trigger cycles or view status.
    """

def handle_portfolio():
    """
    Display current portfolio holdings, value, and P&L.
    Show transaction history.
    """

def main():
    """
    Main loop: display menu, get user choice, call the right handler.
    Keep looping until the user exits.
    """
