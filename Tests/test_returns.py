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
    ticker = 'SPY'
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

def test_get_returns_series():
    """
    Tests the get_returns_series function from the returns module to ensure it calculates daily returns 
    correctly from stock data.
    """
    # Test calculating returns for a known stock data DataFrame
    print("Testing get_returns_series function...")
    stock_data = returns.get_stock_data('SPY', '2023-01-01', '2023-01-10')
    
    returns_series = returns.get_returns_series('SPY', stock_data)
    
    # Check if the returned object is a Series
    assert isinstance(returns_series, pd.Series), "Returned object is not a Series"
    
    # Check if the length of the returns series is one less than the stock data
    assert len(returns_series) == len(stock_data) - 1, "Returns series length is incorrect"
    
    # Check if the first return value is calculated correctly
    # expected_first_return = (152 - 150) / 150
    # assert abs(returns_series.iloc[0] - expected_first_return) < 1e-6, "First return value is incorrect"
    
    print("All tests passed for get_returns_series function.")

if __name__ == "__main__":
    test_get_stock_data()
    test_get_returns_series()