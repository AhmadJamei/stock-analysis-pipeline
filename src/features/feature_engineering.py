import pandas as pd

def create_features(df):
    df = df.copy()

    # Returns
    df["return"] = df["close"].pct_change()

    # Moving averages
    df["ma_5"] = df["close"].rolling(window=5).mean()
    df["ma_10"] = df["close"].rolling(window=10).mean()
    df["ma_20"] = df["close"].rolling(window=20).mean()

    # Volatility
    df["volatility"] = df["return"].rolling(window=5).std()

    # Drop NaN created by rolling
    df = df.dropna()

    print("Features created:")
    print(df.head())

    return df