# pip install yfinance pandas matplotlib

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import yfinance as yf

# --- Parameters ---
symbol = "AAPL"      # e.g. Apple on NASDAQ
# daysBack = 400        # number of days to fetch
interval = "1d"      # options: "1m", "5m", "15m", "1h", "1d"

# --- Fetch data ---
ticker = yf.Ticker(symbol)
# df = ticker.history(period=f"{daysBack}d", interval=interval)
df = yf.download("AAPL", period="600d", interval="1d")

# --- Clean up to match your column names ---
df = df.reset_index()   # reset Date as a column
df = df.rename(columns={
    "Date": "date",
    "Open": "open",
    "High": "high",
    "Low": "low",
    "Close": "close",
    "Volume": "volume"
})

# Drop extra columns if present
df = df[["date", "open", "high", "low", "close", "volume"]]

# --- Show result ---
# print(df.head())

 
# Calculate the moving averages 

df["high_SMA_20"] = df["high"].rolling(window=20).mean()
df["high_SMA_40"] = df["high"].rolling(window=40).mean()
df["high_SMA_60"] = df["high"].rolling(window=60).mean()
df["high_SMA_100"] = df["high"].rolling(window=100).mean()


# Plot 2
plt.figure(figsize=(10,5))
plt.plot(df["date"], df["high"], color="black", label="High Price")
plt.plot(df["date"], df["high_SMA_20"], color="blue", label="SMA 20")
plt.plot(df["date"], df["high_SMA_40"], color="red", label="SMA 40")
plt.plot(df["date"], df["high_SMA_60"], color="green", label="SMA 60")
plt.plot(df["date"], df["high_SMA_100"], color="magenta", label="SMA 100")

plt.title("AAPL High Price - Last 600 Days")
plt.xlabel("Date")
plt.ylabel("Price (USD)")

# Format x-axis
plt.gca().xaxis.set_major_locator(mdates.WeekdayLocator(interval=8))  # tick every 2 weeks
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
plt.gcf().autofmt_xdate()  # auto rotate for readability

plt.legend()
plt.grid(True)

plt.savefig("../plots/aapl_high_price_and_SMA.pdf", dpi=300, bbox_inches="tight")
# plt.show()