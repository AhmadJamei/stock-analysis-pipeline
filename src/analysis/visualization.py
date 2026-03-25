import seaborn as sns
import matplotlib.pyplot as plt
import os

def plot_correlation(df):
    corr = df.corr()

    print("Correlation Matrix:")
    print(corr)

    print_insights(corr)  # 👈 اینجا صدا زده میشه

    sns.heatmap(corr, annot=True)
    plt.show()


def print_insights(corr):
    print("\nInsights:")

    if corr.loc["close", "ma_5"] > 0.8:
        print("Strong short-term trend (ma_5 highly correlated with close)")

    if corr.loc["volume", "close"] < 0:
        print("Volume negatively correlated with price")

    if corr.loc["volatility", "close"] < 0:
        print("Higher volatility tends to occur when price drops")

def plot_price_with_signals(df):

    plt.figure()

    # قیمت
    plt.plot(df.index, df["close"], label="Close Price")

    # میانگین‌ها
    plt.plot(df.index, df["ma_5"], label="MA 5")
    plt.plot(df.index, df["ma_20"], label="MA 20")

    # سیگنال‌ها (اختیاری ولی حرفه‌ای)
    if "signal" in df.columns:
        buy = df[df["signal"] == 1]
        sell = df[df["signal"] == -1]

        plt.scatter(buy.index, buy["close"], marker="^")   # خرید
        plt.scatter(sell.index, sell["close"], marker="v")  # فروش

    plt.title("Stock Price with Moving Averages")
    plt.legend()
    plt.show()

def plot_correlation(df):

    os.makedirs("assets", exist_ok=True)

    plt.figure(figsize=(8,6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")

    plt.title("Correlation Heatmap")
    plt.savefig("assets/correlation.png", bbox_inches="tight")
    plt.close()

def plot_price_with_signals(df):

    os.makedirs("assets", exist_ok=True)

    plt.figure(figsize=(12,5))

    plt.plot(df.index, df["close"], label="Close")
    plt.plot(df.index, df["ma_5"], label="MA 5")
    plt.plot(df.index, df["ma_10"], label="MA 10")

    plt.legend()
    plt.title("Price with Moving Averages")

    plt.savefig("assets/price_chart.png", bbox_inches="tight")
    plt.close()

def plot_signals(df):
 
    if "signal" not in df.columns:
        return

    os.makedirs("assets", exist_ok=True)

    buy = df[df["signal"] == 1]
    sell = df[df["signal"] == -1]

    plt.figure(figsize=(12,5))

    plt.plot(df.index, df["close"], label="Close")
    plt.scatter(buy.index, buy["close"], marker="^", label="Buy")
    plt.scatter(sell.index, sell["close"], marker="v", label="Sell")

    plt.legend()
    plt.title("Trading Signals")

    plt.savefig("assets/signals.png", bbox_inches="tight")
    plt.close()