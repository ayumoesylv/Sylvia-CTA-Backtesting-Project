from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import returns
import pandas as pd


def test_get_stock_data():
    """
    Tests the get_stock_data function from the returns module to ensure it retrieves stock data 
    correctly for a given ticker and date range.
    """
    # Test fetching stock data for a known ticker and date range
    print("Testing get_stock_data function...")
    ticker = 'AAPL'
    start_date = '2023-01-01'
    end_date = '2023-01-10'
    
    stock_data = returns.get_stock_data(ticker, start_date, end_date)
    
    # Check if the returned object is a DataFrame
    assert isinstance(stock_data, pd.DataFrame), "Returned object is not a DataFrame"
    
    # Check if the DataFrame has the expected columns
    expected_columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    for column in expected_columns:
        assert column in stock_data.columns, f"Missing expected column: {column}"
    
    # Check if the DataFrame has data for the specified date range
    assert not stock_data.empty, "DataFrame is empty"
    assert stock_data.index.min() >= pd.to_datetime(start_date), "DataFrame contains dates before start_date"
    assert stock_data.index.max() <= pd.to_datetime(end_date), "DataFrame contains dates after end_date"
    print("All tests passed for get_stock_data function.")

if __name__ == "__main__":
    test_get_stock_data()