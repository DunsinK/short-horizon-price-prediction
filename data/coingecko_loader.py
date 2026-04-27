import requests
import pandas as pd

def get_crypto_data(coin_id="bitcoin", days="365", vs_currency="usd"):
    """
    Fetches historical price data from CoinGecko and returns a panda DataFrame for it.
    """
    if(int(days) > 365):
        print("Can't request more than 365 days of information on free API")
        days = "365"
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {
        "vs_currency": vs_currency, 
        "days": days, 
        "interval": "daily"
    }
    
    

    try:
        response = requests.get(url, params=params)
        response.raise_for_status() # Checking for errors
        raw_data = response.json()

        df = pd.DataFrame(raw_data['prices'], columns=['timestamp', 'Close']) # Converting to DataFrame
        
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms') # Formatting
        df.set_index('timestamp', inplace=True)
        df.dropna()
        
        return df

    except Exception as e:
        print(f"Error fetching data: {e}")
        return None
