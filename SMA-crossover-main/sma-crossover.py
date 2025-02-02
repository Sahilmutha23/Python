import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample data (replace this with real price data)
data = {
    'Date': pd.date_range(start='2024-01-01', periods=100),
    'Close': np.random.randn(100).cumsum() + 100
}
df = pd.DataFrame(data)
df.set_index('Date', inplace=True)

# Parameters for SMA
short_window = 20
long_window = 50

# Calculate short and long moving averages
df['SMA20'] = df['Close'].rolling(window=short_window, min_periods=1).mean()
df['SMA50'] = df['Close'].rolling(window=long_window, min_periods=1).mean()

# Generate signals
df['Signal'] = 0
df['Signal'][short_window:] = np.where(df['SMA20'][short_window:] > df['SMA50'][short_window:], 1, 0)
df['Position'] = df['Signal'].diff()

# Plotting
plt.figure(figsize=(14, 7))
plt.plot(df['Close'], label='Close Price', color='gray', alpha=0.5)
plt.plot(df['SMA20'], label='SMA 20', color='blue')
plt.plot(df['SMA50'], label='SMA 50', color='red')

# Plot Buy signals
plt.plot(df[df['Position'] == 1].index,
         df['SMA20'][df['Position'] == 1],
         '^', markersize=10, color='g', label='Buy Signal')

# Plot Sell signals
plt.plot(df[df['Position'] == -1].index,
         df['SMA20'][df['Position'] == -1],
         'v', markersize=10, color='r', label='Sell Signal')

plt.title('SMA Crossover Strategy')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
