from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd
import pytest

import returns


@pytest.mark.integration
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
    close_prices = pd.Series([100.0, 105.0, 102.0], name="close")

    returns_series = returns.get_returns_series(close_prices)

    expected = pd.Series([0.05, -0.02857142857142858], index=[1, 2], name="close")
    pd.testing.assert_series_equal(returns_series, expected)


def test_convert_to_raw_series_from_cta_dataframe():
    """
    Tests that CTA-style lowercase close columns can be converted into a raw close-price Series.
    """
    stock_data = pd.DataFrame({
        "open": [99.0, 104.0, 103.0],
        "high": [101.0, 106.0, 104.0],
        "low": [98.0, 103.0, 101.0],
        "close": [100.0, 105.0, 102.0],
        "volume": [1000, 1100, 1200],
    })

    close_prices = returns.convert_to_raw_series("SPY", stock_data)

    expected = pd.Series([100.0, 105.0, 102.0], name="close")
    pd.testing.assert_series_equal(close_prices, expected)


def test_convert_to_raw_series_from_yfinance_multiindex_dataframe():
    """
    Tests that yfinance-style MultiIndex close columns can be converted into a raw close-price Series.
    """
    columns = pd.MultiIndex.from_tuples([
        ("Close", "SPY"),
        ("Open", "SPY"),
    ])
    stock_data = pd.DataFrame([[100.0, 99.0], [105.0, 104.0], [102.0, 103.0]], columns=columns)

    close_prices = returns.convert_to_raw_series("SPY", stock_data)

    expected = pd.Series([100.0, 105.0, 102.0], name=("Close", "SPY"))
    pd.testing.assert_series_equal(close_prices, expected)

if __name__ == "__main__":
    test_get_stock_data()
    test_get_returns_series()
