import pandas as pd 
import metrics

def get_labeled_table(table, volume_classification, volatility_classification) -> pd.DataFrame:
    """
    Returns a pd.DataFrame that includes the original backtesting results along with the volume and volatility classifications.

    Preconditions:
    - table: pd.DataFrame containing the backtesting results, including positions, cash, asset values, and daily PnL.
    - volume_classification: pd.Series of volume classifications (low, mid, high) with a datetime index.
    - volatility_classification: pd.Series of volatility classifications (low, mid, high) with a datetime index.
    """
    labeled_table = table.copy()
    labeled_table["volume_classification"] = volume_classification
    labeled_table["volatility_classification"] = volatility_classification
    return labeled_table

def analyze_market_environment(labeled_table, group_by="volume_classification"):
    """
    Returns a dictionary that summarizes the backtesting results based on the specified market environment classification.

    Preconditions:
    - labeled_table: pd.DataFrame containing the backtesting results along with volume and volatility classifications.
    - group_by (str): The column name to group by for analysis. Default is "volume_classification".
    """
    grouped = labeled_table.groupby(group_by)
    summary = grouped.apply(lambda x: metrics.summary_metrics(x, initial_cash=x["cash"].iloc[0]))
    summary_dict = summary.to_dict()
    return summary_dict