import numpy as np
import pandas as pd

def WMA(series, period):
    weights = np.arange(1, period + 1)
    return series.rolling(period).apply(lambda x: np.dot(x, weights) / weights.sum(), raw=True)

def HMA(series, period):
    half_length = int(period / 2)
    sqrt_length = int(np.sqrt(period))

    wma_half = WMA(series, half_length)
    wma_full = WMA(series, period)
    diff = 2 * wma_half - wma_full

    return WMA(diff, sqrt_length)

# Example usage
df = pd.DataFrame({'Close': [10, 11, 12, 11, 13, 15, 14, 16, 17, 18]})
df['HMA_9'] = HMA(df['Close'], 9)
print(df)
