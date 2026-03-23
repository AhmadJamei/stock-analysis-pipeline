import requests
import pandas as pd
import os
from config import API_KEY, BASE_URL

def fetch_stock(symbol="AAPL"):
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": API_KEY,
        "outputsize": "compact"
    }

    response = requests.get(BASE_URL, params=params)

    print("Status:", response.status_code)

    try:
        data = response.json()
    except Exception:
        raise Exception("Invalid JSON response")

    if "Time Series (Daily)" not in data:
        print("API ERROR:", data)
        raise Exception("API response invalid")

    df = pd.DataFrame(data["Time Series (Daily)"]).T
    df.index = pd.to_datetime(df.index)

    df = df.rename(columns={
        "1. open": "open",
        "2. high": "high",
        "3. low": "low",
        "4. close": "close",
        "5. volume": "volume"
    })

    df = df.astype(float)
    # If project is not make it
    os.makedirs("data/raw", exist_ok=True)

    # save data
    file_path = f"data/raw/{symbol}.csv"
    df.to_csv(file_path)

    print(f"Data saved to {file_path}")

    return df