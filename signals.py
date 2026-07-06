# Imports
import pandas as pd

def momentum_signal(prices, window=20):
    """
    Returns a pd.Series object representing the trading signals based on momentum strategy.

    1 indicates a buy signal, -1 indicates a sell signal, and 0 indicates no action.

    Preconditions:
    prices (pd.Series): A pandas Series containing the historical stock prices. 
        prices must be of the same length as the signal series and have at least `window` number of data points.
    window (int): The lookback period for calculating momentum. Default is 20.
    """
    # Calculate momentum using percentage-return momentum defintion
    momentum = prices / prices.shift(window) - 1

    # Generate signals
    signal = pd.Series(0, index=prices.index)
    signal[momentum > 0] = 1  # Buy signal
    signal[momentum < 0] = -1  # Sell signal

    # account for transaction costs 
    # account for execution delay 

    return signal

def macd_signal(prices, short_window=12, long_window=26, signal_window=9):
    """
    Returns a pd.Series object representing the trading signals based on the MACD strategy.

    1 indicates a buy signal, -1 indicates a sell signal, and 0 indicates no action.

    Preconditions:
    prices (pd.Series): A pandas Series containing the historical stock prices.
    short_window (int): The short-term EMA window. Default is 12.
    long_window (int): The long-term EMA window. Default is 26.
    signal_window (int): The signal line EMA window. Default is 9.
    """
    # Calculate short-term and long-term EMAs
    short_ema = prices.ewm(span=short_window, adjust=False).mean()
    long_ema = prices.ewm(span=long_window, adjust=False).mean()

    # Calculate MACD and Signal line
    macd = short_ema - long_ema
    signal_line = macd.ewm(span=signal_window, adjust=False).mean()

    # Generate signals
    signal = pd.Series(0, index=prices.index)
    signal[macd > signal_line] = 1  # Buy signal
    signal[macd < signal_line] = -1  # Sell signal

    return signal