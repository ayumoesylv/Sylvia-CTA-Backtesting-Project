from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import backtester 
import pandas as pd

def test_backtester_initialization():
    """
    Tests the initialization of the Backtester class to ensure it correctly sets up the backtesting environment.
    """
    # Test data for initialization
    prices = pd.Series([100, 101, 102, 103, 104], index=pd.date_range(start='2023-01-01', periods=5))
    signal = pd.Series([0, 1, 0, -1, 0], index=pd.date_range(start='2023-01-01', periods=5))
    
    # Initialize the Backtester
    bt = backtester.Backtester(prices, signal)
    
    # Check if the table DataFrame is created with the correct index
    assert isinstance(bt.table, pd.DataFrame), "Backtester table is not a DataFrame"
    assert all(bt.table.index == prices.index), "Backtester table index does not match prices index"
    
    # Check if the prices and signal columns are correctly set
    assert 'prices' in bt.table.columns, "Backtester table missing 'prices' column"
    assert 'signal' in bt.table.columns, "Backtester table missing 'signal' column"
    
    # Check if initial cash is set correctly
    assert bt.initial_cash == 100000, "Initial cash is not set correctly"
    
    print("All tests passed for Backtester initialization.")

def test_run_backtest():
    # Test data for initialization
    prices = pd.Series([100, 101, 102, 103, 104], index=pd.date_range(start='2023-01-01', periods=5))
    signal = pd.Series([0, 1, 0, -1, 0], index=pd.date_range(start='2023-01-01', periods=5))

    # Initialize the Backtester
    bt = backtester.Backtester(prices, signal)

    # Run the backtest
    bt.run_backtest()

    # Check if the table DataFrame is created with the correct index
    assert isinstance(bt.table, pd.DataFrame), "Backtester table is not a DataFrame"
    assert all(bt.table.index == prices.index), "Backtester table index does not match prices index"

    # Check if the prices and signal columns are correctly set
    assert 'prices' in bt.table.columns, "Backtester table missing 'prices' column"
    assert 'signal' in bt.table.columns, "Backtester table missing 'signal' column"

    # Check if initial cash is set correctly
    assert bt.initial_cash == 100000, "Initial cash is not set correctly"

    print("All tests passed for Backtester run_backtest.")

def test_summary_metrics():
    # Test data for initialization
    prices = pd.Series([100, 101, 102, 103, 104], index=pd.date_range(start='2023-01-01', periods=5))
    signal = pd.Series([0, 1, 0, -1, 0], index=pd.date_range(start='2023-01-01', periods=5))

    # Initialize the Backtester
    bt = backtester.Backtester(prices, signal)

    # Run the backtest
    bt.run_backtest()

    # Get summary metrics
    metrics = bt.summary_metrics()

    # Check if the metrics dictionary contains expected keys
    expected_keys = ['total_return', 'annual_volatility', 'annual_sharpe', 'max_drawdown', 'average_turnover', 'total_turnover', 'trade_frequency']
    assert all(key in metrics for key in expected_keys), "Summary metrics missing expected keys"

    print("All tests passed for Backtester summary_metrics.")

def test_print_backtest_results():
    # Test data for initialization
    prices = pd.Series([100, 101, 102, 103, 104], index=pd.date_range(start='2023-01-01', periods=5))
    signal = pd.Series([0, 1, 0, -1, 0], index=pd.date_range(start='2023-01-01', periods=5))

    # Initialize the Backtester
    bt = backtester.Backtester(prices, signal)

    # Run the backtest
    bt.run_backtest()

    # Print the backtest results
    bt.print_backtest_results()



if __name__ == "__main__":
    test_backtester_initialization()
    test_run_backtest()
    test_summary_metrics()
    test_print_backtest_results()
