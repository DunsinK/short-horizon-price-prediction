import yfinance as yf

aapl = yf.Ticker("Nvia")
data = aapl.history(period="1mo")
print(data)