import matplotlib.pyplot as plt

def plot_price(df):
    df["close"].plot(title="Stock Price")
    plt.show()