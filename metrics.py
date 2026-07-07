import pandas as pd

def summary_metrics(table: pd.DataFrame, initial_cash: float) -> dict:
        """
        Returns a dictionary containing summary metrics of the backtesting results, such as volatility, 
        Sharpe, drawdown, turnover, and trade frequency.

        Preconditions:
        - table: pd.DataFrame containing the backtesting results, including positions, cash, asset values, and daily PnL.
        - initial_cash: float representing the initial cash balance for the backtest.
        """

        # Calculate total returns
        total_return = (table["total_portfolio_value"].iloc[-1] / initial_cash) - 1
        # Create daily returns pandas series 
        daily_returns = table["total_portfolio_value"].pct_change().dropna()
        # volatility, Sharpe, drawdown, turnover, and trade frequency
        annual_volatility = daily_returns.std() * (252 ** 0.5)
        annual_sharpe = daily_returns.mean() / daily_returns.std() * (252 ** 0.5)
        running_max = table["total_portfolio_value"].cummax()
        drawdown = table["total_portfolio_value"] / running_max - 1
        max_drawdown = drawdown.min()

        turnover = table["position"].diff().abs()
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