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