import yfinance as yf
import pandas as pd

def get_stock_data(ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Fetches historical stock data for a given ticker symbol between specified start and end dates.

    Parameters:
    ticker (str): The stock ticker symbol (e.g., 'AAPL' for Apple Inc.).
    start_date (str): The start date for fetching data in 'YYYY-MM-DD' format.
    end_date (str): The end date for fetching data in 'YYYY-MM-DD' format.

    Returns:
    pd.DataFrame: A DataFrame containing the historical stock data.
    """
    stock_data = yf.download(ticker, start=start_date, end=end_date, auto_adjust=True)
    return stock_data


def get_returns_series(ticker: str, stock_data: pd.DataFrame) -> pd.Series:
    """
    Returns the daily returns of the stock based on adjusted closing prices as pd.Series object. Read-only 
    function. 

    Preconditions: 
    `ticker` must be a valid stock ticker symbol, and `stock_data` must be a DataFrame containing historical stock data with an `Close` column that is auto-adjusted.
    `stock_data` must be a DataFrame containing historical stock data with an `Close` column that is auto-adjusted.
    """
    assert isinstance(stock_data, pd.DataFrame), "Input must be a pandas DataFrame"
    assert 'Close' in stock_data.columns, "DataFrame must contain a 'Close' column"
    returns = stock_data[('Close', ticker)].pct_change().dropna()
    return returns

def print_stock_data_with_returns(stock_data: pd.DataFrame):
    """
    Prints the stock data along with the calculated daily returns.

    Parameters:
    stock_data (pd.DataFrame): A DataFrame containing historical stock data.
    """
    returns_series = get_returns_series(stock_data)
    combined_data = stock_data.copy()
    combined_data['Returns'] = returns_series
    print(combined_data.head(20))

if __name__ == "__main__":
    # Example usage
    ticker = 'SPY'
    start_date = '2016-07-04'
    end_date = '2026-07-04'
    
    stock_data = get_stock_data(ticker, start_date, end_date)
    print_stock_data_with_returns(stock_data)
