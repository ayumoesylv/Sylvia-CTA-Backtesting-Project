from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import signals
import pandas as pd

def test_momentum_signal():
    # Test data for momentum signal
    prices = pd.Series([100, 101, 102, 103, 104], index=pd.date_range(start='2023-01-01', periods=5))
    
    # Generate momentum signal
    signal = signals.momentum_signal(prices, window=2)
    
    # Check if the signal is a pandas Series
    assert isinstance(signal, pd.Series), "Momentum signal is not a pandas Series"
    
    # Check if the signal has the same index as prices
    assert all(signal.index == prices.index), "Momentum signal index does not match prices index"
    
    print("All tests passed for momentum_signal.")

def test_macd_signal():
    # Test data for MACD signal
    prices = pd.Series([100, 101, 102, 103, 104], index=pd.date_range(start='2023-01-01', periods=5))
    
    # Generate MACD signal
    signal = signals.macd_signal(prices)
    
    # Check if the signal is a pandas Series
    assert isinstance(signal, pd.Series), "MACD signal is not a pandas Series"
    
    # Check if the signal has the same index as prices
    assert all(signal.index == prices.index), "MACD signal index does not match prices index"
    
    print("All tests passed for macd_signal.")

if __name__ == "__main__":
    test_momentum_signal()
    test_macd_signal()