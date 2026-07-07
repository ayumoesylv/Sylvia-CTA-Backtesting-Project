from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import market_env_label
import pandas as pd

def test_get_rolling_volume():
    # Test data for rolling volume
    volume_data = pd.Series([1000, 2000, 1500, 3000, 2500], index=pd.date_range(start='2023-01-01', periods=5))
    
    # Get rolling volume
    rolling_volume = market_env_label.get_rolling_volume(volume_data, window=2)
    
    # Check if the rolling volume is a pandas Series
    assert isinstance(rolling_volume, pd.Series), "Rolling volume is not a pandas Series"
    
    # Check if the rolling volume has the same index as the original volume data
    assert all(rolling_volume.index == volume_data.index), "Rolling volume index does not match original volume data index"
    
    print("All tests passed for get_rolling_volume function.")

def test_get_volume_classification():
    # Test data for volume classification
    volume_data = pd.Series([1000, 2000, 1500, 3000, 2500], index=pd.date_range(start='2023-01-01', periods=5))
    
    # Get rolling volume
    rolling_volume = market_env_label.get_rolling_volume(volume_data, window=2)
    
    # Get volume classification
    volume_classification = market_env_label.get_volume_classification(rolling_volume)
    
    # Check if the classification is a pandas Series
    assert isinstance(volume_classification, pd.Series), "Volume classification is not a pandas Series"
    
    # Check if the classification has the same index as rolling volume
    assert all(volume_classification.index == rolling_volume.index), "Volume classification index does not match rolling volume index"
    
    print("All tests passed for get_volume_classification function.")

def test_get_rolling_volatility():
    # Test data for rolling volatility
    price_data = pd.Series([100, 101, 102, 103, 104], index=pd.date_range(start='2023-01-01', periods=5))
    
    # Get rolling volatility
    rolling_volatility = market_env_label.get_rolling_volatility(price_data, window=2)
    
    # Check if the rolling volatility is a pandas Series
    assert isinstance(rolling_volatility, pd.Series), "Rolling volatility is not a pandas Series"
    
    # Check if the rolling volatility has the same index as the original price data
    assert all(rolling_volatility.index == price_data.index), "Rolling volatility index does not match original price data index"
    
    print("All tests passed for get_rolling_volatility function.")

def test_get_volatility_classification():
    # Test data for volatility classification
    price_data = pd.Series([100, 101, 102, 103, 104], index=pd.date_range(start='2023-01-01', periods=5))
    
    # Get rolling volatility
    rolling_volatility = market_env_label.get_rolling_volatility(price_data, window=2)
    
    # Get volatility classification
    volatility_classification = market_env_label.get_volatility_classification(rolling_volatility)
    
    # Check if the classification is a pandas Series
    assert isinstance(volatility_classification, pd.Series), "Volatility classification is not a pandas Series"
    
    # Check if the classification has the same index as rolling volatility
    assert all(volatility_classification.index == rolling_volatility.index), "Volatility classification index does not match rolling volatility index"
    
    print("All tests passed for get_volatility_classification function.")

if __name__ == "__main__":
    test_get_rolling_volume()
    test_get_volume_classification()
    test_get_rolling_volatility()
    test_get_volatility_classification()