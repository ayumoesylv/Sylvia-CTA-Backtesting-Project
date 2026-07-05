# The module containing the backtester class and related functions for backtesting trading strategies.
import pandas as pd

class Backtester:
    """
    Class specifications:

    Class invariants:
    table (pd.DataFrame): A pandas DataFrame containing the backtesting results, including 
        positions, cash, asset values, and daily PnL.
    initial_cash (float): The initial cash balance for the backtesting simulation.
    """
    # CONSTRUCTOR
    def __init__(self, prices, signal, initial_cash=100000):
        # self.prices = prices
        # self.signal = signal
        self.table = pd.DataFrame(index=prices.index)
        self.table["prices"] = prices
        self.table["signal"] = signal
        self.initial_cash = initial_cash

    # PRIVATE HELPER METHODS 
    def _get_position(self):
        """
        Returns a pd.Series object representing the current position based on the trading signals.
        """
        # Implement logic to get the current position
        position = self.table.signal.shift(1).fillna(0)  # Example logic: shift the signal to represent the position
        return position

    def _get_cash(self):
        """
        Returns a pd.Series object representing the current cash balance.
        """
        trades = self._get_position().diff().fillna(self._get_position())  # Calculate trades based on signal changes
        cash = self.initial_cash - (trades * self.table.prices).cumsum()
        return cash

    def _get_asset_value(self):
        """
        Returns a pd.Series object representing the current asset value.
        """
        # Implement logic to get the current asset value
        asset_value = self._get_position() * self.table.prices
        return asset_value

    def _get_total_portfolio_value(self):
        """
        Returns a pd.Series object representing the total portfolio value.
        """
        # Implement logic to get the total portfolio value
        portfolio_value = self._get_cash() + self._get_asset_value()
        return portfolio_value

    def _get_daily_pnl(self):
        """
        Returns a pd.Series object representing the daily profit and loss.
        """
        # Implement logic to get the daily profit and loss
        daily_pnl = self._get_total_portfolio_value().diff().fillna(0)
        return daily_pnl

    # METHODS
    def run_backtest(self):
        """
        Returns a pd.DataFrame object containing the backtesting results, including positions, cash, asset values, and daily PnL.
        """
        # Implement the backtesting logic here
        self.table["position"] = self._get_position()
        self.table["cash"] = self._get_cash()
        self.table["asset_value"] = self._get_asset_value()
        self.table["total_portfolio_value"] = self._get_total_portfolio_value()
        self.table["daily_pnl"] = self._get_daily_pnl()

        return self.table

    def print_backtest_results(self):
        """
        Prints the backtesting results in a readable format.
        """
        # Implement logic to print the backtesting results
        print(self.table.head(20))  # Print the first 20 rows of the backtesting results

    def evaluate_performance(self):
        # Implement performance evaluation logic here
        pass