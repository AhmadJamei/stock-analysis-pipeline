import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.rename(columns={
        "1. open": "open",
        "2. high": "high",
        "3. low": "low",
        "4. close": "close",
        "5. volume": "volume"
    })

    df = df.astype(float)

    df["return"] = df["close"].pct_change()
    df["ma_5"] = df["close"].rolling(5).mean()
    df["volatility"] = df["return"].rolling(5).std()

    return df