from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import metrics
import pandas as pd

def test_summary_metrics():
    # Test data for summary_metrics method
    prices = pd.Series([100, 101, 102, 103, 104], index=pd.date_range(start='2023-01-01', periods=5))
    signal = pd.Series([1, 1, -1, -1, 1], index=pd.date_range(start='2023-01-01', periods=5))
    
    # Create a DataFrame to simulate backtesting results
    table = pd.DataFrame({
        "prices": prices,
        "signal": signal,
        "position": signal.shift(1).fillna(0),
        "cash": 100000 - (signal.shift(1).fillna(0) * prices).cumsum(),
        "asset_value": signal.shift(1).fillna(0) * prices,
        "total_portfolio_value": (100000 - (signal.shift(1).fillna(0) * prices).cumsum()) + (signal.shift(1).fillna(0) * prices),
        "daily_pnl": ((100000 - (signal.shift(1).fillna(0) * prices).cumsum()) + (signal.shift(1).fillna(0) * prices)).diff().fillna(0)
    })
    
    initial_cash = 100000
    
    # Calculate summary metrics
    metrics_dict = metrics.summary_metrics(table, initial_cash)
    
    # Check if the returned object is a dictionary
    assert isinstance(metrics_dict, dict), "Summary metrics result is not a dictionary"
    
    # Check if the dictionary contains expected keys
    expected_keys = ["total_return", "annual_volatility", "annual_sharpe", "max_drawdown", "average_turnover", "total_turnover", "trade_frequency"]
    assert all(key in metrics_dict for key in expected_keys), "Summary metrics dictionary does not contain all expected keys"
    
    print("All tests passed for summary_metrics function.")

if __name__ == "__main__":
    test_summary_metrics()