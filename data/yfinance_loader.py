import yfinance as yf

def get_stock_data(Tick="QQQ",period="1y",interval="1d"):
    """
        Fetches historical price data from YahooFinance and returns a panda DataFrame for it.
    """
    data = yf.download(Tick, period=period, interval=interval) # example data = yf.download("AAPL", period="1y", interval="1d")
    data.dropna()
    return data


