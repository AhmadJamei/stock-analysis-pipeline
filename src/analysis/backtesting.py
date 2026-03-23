import numpy as np

def backtest_strategy(df):
    print("FUCT RUNNED")
    df = df.copy()

    # استراتژی (بر اساس کراس MA)
    df["signal"] = 0
    df.loc[df["ma_5"] > df["ma_20"], "signal"] = 1
    df.loc[df["ma_5"] < df["ma_20"], "signal"] = -1

    # بازده استراتژی
    df["strategy_return"] = df["return"] * df["signal"].shift(1)

    # حذف NaN
    df = df.dropna()

    # بازده تجمعی
    df["cumulative_return"] = (1 + df["strategy_return"]).cumprod()

    # --- METRICS ---

    total_return = df["cumulative_return"].iloc[-1] - 1

    sharpe_ratio = (
        df["strategy_return"].mean() / df["strategy_return"].std()
    ) * np.sqrt(252)

    # Max Drawdown
    cumulative_max = df["cumulative_return"].cummax()
    drawdown = df["cumulative_return"] / cumulative_max - 1
    max_drawdown = drawdown.min()

    # Win Rate
    win_rate = (df["strategy_return"] > 0).mean()

    # چاپ نتایج
    print("\n--- Backtesting Results ---")
    print(f"Total Return: {total_return:.2%}")
    print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
    print(f"Max Drawdown: {max_drawdown:.2%}")
    print(f"Win Rate: {win_rate:.2%}")

    return df