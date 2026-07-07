# function that will return a pd series of classifications for each daily price for whether volume is high or low bsaed on window
import pandas as pd

def get_rolling_volume(volume: pd.Series, window: int = 20) -> pd.Series:
    """
    Returns a pd.Series of rolling average volume over a specified window.
    
    Preconditions:
    - volume: pd.Series of daily volumes with a datetime index. Requires same dimension as corresponding price index.
    - window (int): The rolling window size for calculating the volume average. Default is 20 days.
    """
    return volume.rolling(window=window).mean()

def get_volume_classification(rolling_volume: pd.Series, low_q = 0.25, high_q = 0.75) -> pd.Series:
    """
    Returns a pd.Series of classifications (low, mid, high) for each daily price based on
    the rolling average volume over a specified window.
    
    Preconditions:
    - rolling_volume: pd.Series of rolling average volumes with a datetime index.
    - window (int): The rolling window size for calculating the volume average. Default is 20 days.
    """
    low = rolling_volume.quantile(low_q)
    high = rolling_volume.quantile(high_q)

    # Classify volume based on quantiles 
    regime = pd.Series("mid volume", index=rolling_volume.index)
    regime[rolling_volume <= low] = "low volume"
    regime[rolling_volume >= high] = "high volume"
    regime[rolling_volume.isna()] = pd.NA
    return regime

def get_rolling_volatility(prices: pd.Series, window: int = 20) -> pd.Series:
    """
    Returns a pd.Series of rolling volatility over a specified window.
    
    Preconditions:
    - prices: pd.Series of daily prices with a datetime index. Requires same dimension as corresponding volume index.
    - window (int): The rolling window size for calculating the volatility. Default is 20 days.
    """
    return prices.pct_change().rolling(window=window).std()

def get_volatility_classification(rolling_volatility: pd.Series, low_q = 0.25, high_q = 0.75) -> pd.Series: 
    """
    Returns a pd.Series of classifications (low, mid, high) for each daily price based on
    the rolling volatility over a specified window.
    
    Preconditions:
    - rolling_volatility: pd.Series of rolling volatilities with a datetime index.
    - window (int): The rolling window size for calculating the volatility. Default is 20 days.
    """
    low = rolling_volatility.quantile(low_q)
    high = rolling_volatility.quantile(high_q)

    # Classify volatility based on quantiles 
    regime = pd.Series("mid volatility", index=rolling_volatility.index)
    regime[rolling_volatility <= low] = "low volatility"
    regime[rolling_volatility >= high] = "high volatility"
    regime[rolling_volatility.isna()] = pd.NA
    return regime