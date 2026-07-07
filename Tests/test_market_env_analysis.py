from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import market_env_analysis
import pandas as pd

def test_get_labeled_table():
    # Test data for get_labeled_table method
    table = pd.DataFrame({
        "position": [1, 1, -1, -1, 1],
        "cash": [100000, 99900, 99800, 99700, 99600],
        "asset_value": [1000, 2000, 1500, 3000, 2500],
        "total_portfolio_value": [101000, 101900, 99900, 102700, 102100],
        "daily_pnl": [1000, 900, -1900, 2800, -600]
    }, index=pd.date_range(start='2023-01-01', periods=5))
    
    volume_classification = pd.Series(["low", "mid", "high", "mid", "low"], index=pd.date_range(start='2023-01-01', periods=5))
    volatility_classification = pd.Series(["low", "low", "high", "high", "mid"], index=pd.date_range(start='2023-01-01', periods=5))
    
    # Get labeled table
    labeled_table = market_env_analysis.get_labeled_table(table, volume_classification, volatility_classification)
    
    # Check if the labeled table is a pandas DataFrame
    assert isinstance(labeled_table, pd.DataFrame), "Labeled table is not a pandas DataFrame"
    
    # Check if the labeled table has the expected columns
    expected_columns = ['position', 'cash', 'asset_value', 'total_portfolio_value', 'daily_pnl', 'volume_classification', 'volatility_classification']
    assert all(col in labeled_table.columns for col in expected_columns), "Labeled table does not have the expected columns"
    
    print("All tests passed for get_labeled_table function.")

def test_analyze_market_environment():
    # Test data for analyze_market_environment method
    labeled_table = pd.DataFrame({
        "position": [1, 1, -1, -1, 1],
        "cash": [100000, 99900, 99800, 99700, 99600],
        "asset_value": [1000, 2000, 1500, 3000, 2500],
        "total_portfolio_value": [101000, 101900, 99900, 102700, 102100],
        "daily_pnl": [1000, 900, -1900, 2800, -600],
        "volume_classification": ["low", "mid", "high", "mid", "low"],
        "volatility_classification": ["low", "low", "high", "high", "mid"]
    }, index=pd.date_range(start='2023-01-01', periods=5))
    
    # Analyze market environment
    summary = market_env_analysis.analyze_market_environment(labeled_table)
    
    # Check if the summary is a pandas DataFrame
    assert isinstance(summary, dict), "Summary is not a dictionary"
    
    print("All tests passed for analyze_market_environment function.")

if __name__ == "__main__":
    test_get_labeled_table()
    test_analyze_market_environment() 