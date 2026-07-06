from backtester import Backtester
import pandas as pd

class RealisticBacktester(Backtester):
    """
    A class for backtesting trading strategies with realistic assumptions, including transaction costs and slippage.

    Inherits from the Backtester class.

    Attributes:
        table (pd.DataFrame): A pandas DataFrame containing the backtesting results, including 
            positions, cash, asset values, and daily PnL.
        initial_cash (float): The initial cash balance for the backtesting simulation.
        cost_per_trade (float): The cost per trade for the backtesting simulation.
        slippage (float): The slippage percentage for the backtesting simulation.
    """
    
    def __init__(self, prices, signal, initial_cash=100000, cost_per_trade=10, slippage=0.001):
        """
        Initializes the RealisticBacktester with prices, signal, initial cash, cost per trade, and slippage.

        Parameters:
            prices (numeric pd.Series): A pandas Series containing the historical stock prices.
            signal (numeric pd.Series): A pandas Series containing the trading signals.
            initial_cash (float): The initial cash balance for the backtesting simulation. Default is 100000.
            cost_per_trade (float): The cost per trade for the backtesting simulation. Default is 10.
            slippage (float): The slippage percentage for the backtesting simulation. Default is 0.001 (0.1%).
        """
        assert isinstance(prices, pd.Series), "Prices must be a pandas Series"
        assert isinstance(signal, pd.Series), "Signal must be a pandas Series"
        assert all(prices.index == signal.index), "Prices and signal must have the same index"
        assert isinstance(initial_cash, (int, float)), "Initial cash must be a number"
        # assert isinstance(prices.iloc[0], (int, float)), "Prices must be numeric"
        # print(signal.iloc[0])
        # print(type(signal.iloc[0]))
        # print(prices.iloc[0])
        # print(type(prices.iloc[0]))
        # assert isinstance(signal.iloc[1], (int, float)), "Signal must be numeric"
        # assert isinstance(cost_per_trade, (int, float)), "Cost per trade must be a number"
        # assert isinstance(slippage, (int, float)), "Slippage must be a number"
        super().__init__(prices, signal, initial_cash)
        self.cost_per_trade = cost_per_trade
        self.slippage = slippage

    def _get_cash(self):
        """
        Returns a pd.Series object representing the current cash balance, accounting for transaction costs and slippage.
        """
        position = self._get_position()
        trades = position.diff().fillna(position)

        execution_price = self.table.prices.astype(float).copy()
        execution_price[trades > 0] = self.table.prices[trades > 0] * (1 + self.slippage)
        execution_price[trades < 0] = self.table.prices[trades < 0] * (1 - self.slippage)

        trade_value = trades * execution_price
        transaction_cost = trades.abs() * self.cost_per_trade

        cash = (
            self.initial_cash
            - trade_value.cumsum()
            - transaction_cost.cumsum()
        )
        return cash