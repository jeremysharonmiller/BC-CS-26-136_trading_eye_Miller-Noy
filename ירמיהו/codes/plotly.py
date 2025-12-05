import yfinance as yf
import plotly.graph_objects as go

df = yf.download("AAPL", period="6mo")

df["SMA20"] = df["Close"].rolling(20).mean()
df = df.reset_index()

fig = go.Figure()

fig.add_trace(go.Scatter(x=df["Date"], y=df["Close"],
                         mode="lines", name="Close", line=dict(color="white")))

fig.add_trace(go.Scatter(x=df["Date"], y=df["SMA20"],
                         mode="lines", name="SMA20", line=dict(color="orange")))

fig.update_layout(title="AAPL — Example Plotly Chart", template="plotly_dark")
fig.show()
