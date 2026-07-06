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
        """
        prices (numeric pd.Series): A pandas Series containing the historical stock prices.
        signal (numeric pd.Series): A pandas Series containing the trading signals.
        initial_cash (float): The initial cash balance for the backtesting simulation. Default is 100000.
        """
        # self.prices = prices
        # self.signal = signal
        assert isinstance(prices, pd.Series), "Prices must be a pandas Series"
        assert isinstance(signal, pd.Series), "Signal must be a pandas Series"
        assert all(prices.index == signal.index), "Prices and signal must have the same index"
        # assert isinstance(initial_cash, (int, float)), "Initial cash must be a number"
        # assert isinstance(prices.iloc[0], (int, float)), "Prices must be numeric"
        # assert isinstance(signal.iloc[1], (int, float)), "Signal must be numeric"
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

    def summary_metrics(self):
        """
        Returns a dictionary containing summary metrics of the backtesting results, such as volatility, 
        Sharpe, drawdown, turnover, and trade frequency.
        """        
        # Calculate total returns
        total_return = (self.table["total_portfolio_value"].iloc[-1] / self.initial_cash) - 1
        # Create daily returns pandas series 
        daily_returns = self.table["total_portfolio_value"].pct_change().dropna()
        # volatility, Sharpe, drawdown, turnover, and trade frequency
        annual_volatility = daily_returns.std() * (252 ** 0.5)
        annual_sharpe = daily_returns.mean() / daily_returns.std() * (252 ** 0.5)
        running_max = self.table["total_portfolio_value"].cummax()
        drawdown = self.table["total_portfolio_value"] / running_max - 1
        max_drawdown = drawdown.min()

        turnover = self.table["position"].diff().abs()
        average_turnover = turnover.mean()
        total_turnover = turnover.sum()
        trade_frequency = turnover[turnover > 0].sum() / len(turnover)

        metrics = {
            "total_return": total_return,
            "annual_volatility": annual_volatility,
            "annual_sharpe": annual_sharpe,
            "max_drawdown": max_drawdown,
            "average_turnover": average_turnover,
            "total_turnover": total_turnover,
            "trade_frequency": trade_frequency
        }
        return metrics

    def print_backtest_results(self):
        """
        Prints the backtesting results in a readable format.
        """
        # Implement logic to print the backtesting results
        print(self.table.head(10))  # Print the first 20 rows of the backtesting results
        print("\nSummary Metrics:")
        for key, value in self.summary_metrics().items():
            print(f"{key}: {value}")
