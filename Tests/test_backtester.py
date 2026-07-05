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
    test_print_backtest_results()
