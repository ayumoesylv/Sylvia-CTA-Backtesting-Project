## 07.04.2026
## Decision 1 - 

Decided to use long, short, flat strategy rather than long only strategy

## Decision 2 - 

Decided to use percentage-return momentum is preferred because it is scale-invariant over prices.diff(window)

## 07.05.2026
## Decision 3 - 

Decided to use a jupyter notebook as the strategy driver rather than specialized module

Reason: When building AI models don't want to have to reload everytime I want to change something 

## Decision 4 - 

Decided to let my backtester class expose public facing methods to evaluate the strategy

Reason: ??

## Decision 5 - 

Decided to create a subclass RealsticBacktester extending Backtester instead of modifying backtester code directly for ease of editing 

## 07.06.2026
## Decision 6 - 

Decided to make execution prices floats before modifying them 

Reason: execution prices in realistic backtester was being interpreted as int64, causing bug with float being assigned to it

## Decision 7 - 

Decided to create market_env_label.py and market_env_analysis.py files 

Reason: market_regime_label will add columns that categorize daily returns in terms of high or low volume or volatility. Analysis.py will take those labels and determine performance in different market regimes. 

## 07.07.2026
## Decisio 8 - Separate portfolio simulation from performance evaluation

**Status:** Accepted

### Context

Initially, the `Backtester` class was responsible for both simulating trades and computing performance metrics such as total return, Sharpe ratio, volatility, and drawdown.

As the project evolved to include market regime analysis (e.g., evaluating strategy performance during high-volatility versus low-volatility periods), this coupling became problematic. The backtester simulates one continuous portfolio through time, while performance metrics may need to be computed on arbitrary subsets of the resulting time series.

### Decision

The `Backtester` will be responsible **only** for portfolio simulation.

It will output a complete results DataFrame containing quantities such as:

- Position
- Trades
- Cash
- Asset Value
- Total Portfolio Value
- Daily PnL
- Daily Returns

Performance statistics (e.g., total return, volatility, Sharpe ratio, drawdown, turnover, trade frequency) will be implemented separately in `metrics.py`.

The `analysis.py` module will use these metrics to evaluate different experiments, parameter choices, and market regimes without rerunning the backtester.

### Rationale

This separates concerns according to the Single Responsibility Principle:

- **Backtester:** Simulate portfolio evolution.
- **Metrics:** Summarize portfolio performance.
- **Analysis:** Compare strategies, parameters, and market regimes.
- **Features:** Generate market features and regime labels.
- **Strategies:** Generate trading signals.

This design makes the backtester reusable and allows the same portfolio history to be analyzed in multiple ways (e.g., only high-volatility periods, only low-volume periods, different parameter sweeps) without changing the simulation.

### Consequences

**Advantages**
- Cleaner separation of responsibilities.
- Easier testing of individual components.
- Metrics can be computed on any subset of the results DataFrame.
- Future strategies and analyses can reuse the same backtester.
- New performance metrics can be added without modifying simulation logic.

**Trade-offs**
- Slightly more modules and function calls.
- Requires passing the results DataFrame into metric functions rather than exposing them directly through the backtester.