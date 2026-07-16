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


def get_returns_series(close_data: pd.Series) -> pd.Series:
    """
    Returns daily asset returns based on a close-price Series.

    Preconditions: 
    `close_data` must be a pandas Series containing close prices.
    """
    assert isinstance(close_data, pd.Series), "Input must be a pandas Series"
    returns = close_data.pct_change().dropna()
    return returns

def convert_to_raw_series(ticker: str, stock_data: pd.DataFrame) -> pd.Series: 
    """
    Returns the close price column as a pd.Series.

    Preconditions: 
        `stock_data` must be a DataFrame containing close-price data from yfinance or CTA CSVs.
    """
    assert isinstance(stock_data, pd.DataFrame), "Input must be a pandas DataFrame"
    if isinstance(stock_data.columns, pd.MultiIndex):
        if ('Close', ticker) in stock_data.columns:
            return stock_data[('Close', ticker)]
        close_data = stock_data['Close']
        if isinstance(close_data, pd.DataFrame) and len(close_data.columns) == 1:
            return close_data.iloc[:, 0]
        raise KeyError("Ticker is required when DataFrame contains multiple close columns")
    if ('Close', ticker) in stock_data.columns:
        return stock_data[('Close', ticker)]
    if 'Close' in stock_data.columns:
        return stock_data['Close']
    if 'close' in stock_data.columns:
        return stock_data['close']
    raise KeyError("DataFrame must contain a close price column")

def print_stock_data_with_returns(stock_data: pd.DataFrame):
    """
    Prints the stock data along with the calculated daily returns.

    Parameters:
    stock_data (pd.DataFrame): A DataFrame containing historical stock data.
    """
    returns_series = get_returns_series(convert_to_raw_series("", stock_data))
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
