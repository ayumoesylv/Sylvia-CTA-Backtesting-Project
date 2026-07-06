from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import backtester_realistic
import pandas as pd

def test_realistic_backtester():
    # Test data for realistic backtester
    prices = pd.Series([100.0, 101.0, 102.0, 103.0, 104.0], index=pd.date_range(start='2023-01-01', periods=5))
    signal = pd.Series([1, 1, -1, -1, 1], index=pd.date_range(start='2023-01-01', periods=5))
    
    # Initialize RealisticBacktester
    backtester = backtester_realistic.RealisticBacktester(prices, signal, initial_cash=100000, cost_per_trade=10, slippage=0.001)
    
    # Run backtest
    backtester.run_backtest()
    
    # Check if the table attribute is a pandas DataFrame
    assert isinstance(backtester.table, pd.DataFrame), "Backtesting results are not stored in a pandas DataFrame"
    
    # Check if the table has the expected columns
    expected_columns = ['position', 'cash', 'asset_value', 'total_portfolio_value', 'daily_pnl']
    assert all(col in backtester.table.columns for col in expected_columns), "Backtesting results DataFrame does not have the expected columns"
    
    print("All tests passed for RealisticBacktester.")

def test_get_cash():
    # Test data for get_cash method
    prices = pd.Series([100, 101, 102, 103, 104], index=pd.date_range(start='2023-01-01', periods=5))
    signal = pd.Series([1, 1, -1, -1, 1], index=pd.date_range(start='2023-01-01', periods=5))
    
    # Initialize RealisticBacktester
    backtester = backtester_realistic.RealisticBacktester(prices, signal, initial_cash=100000, cost_per_trade=10, slippage=0.001)
    
    # Run backtest
    backtester.run_backtest()
    
    # Get cash series
    cash_series = backtester._get_cash()
    
    # Check if the cash series is a pandas Series
    assert isinstance(cash_series, pd.Series), "Cash series is not a pandas Series"
    
    # Check if the cash series has the same index as prices
    assert all(cash_series.index == prices.index), "Cash series index does not match prices index"
    
    print("All tests passed for _get_cash method.")

def test_summary_metrics():
    # Test data for summary_metrics method
    prices = pd.Series([100, 101, 102, 103, 104], index=pd.date_range(start='2023-01-01', periods=5))
    signal = pd.Series([1, 1, -1, -1, 1], index=pd.date_range(start='2023-01-01', periods=5))
    
    # Initialize RealisticBacktester
    backtester = backtester_realistic.RealisticBacktester(prices, signal, initial_cash=100000, cost_per_trade=10, slippage=0.001)
    
    # Run backtest
    backtester.run_backtest()
    
    # Get summary metrics
    metrics = backtester.summary_metrics()
    
    # Check if the metrics is a dictionary
    assert isinstance(metrics, dict), "Summary metrics is not a dictionary"
    
    # Check if the metrics dictionary has the expected keys
    expected_keys = ['total_return', 'annual_volatility', 'annual_sharpe']
    assert all(key in metrics for key in expected_keys), "Summary metrics dictionary does not have the expected keys"
    
    print("All tests passed for summary_metrics method.")

if __name__ == "__main__":
    test_realistic_backtester()
    test_get_cash()
    test_summary_metrics()