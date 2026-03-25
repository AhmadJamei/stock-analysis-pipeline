import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------
# Page Config
# ----------------------
st.set_page_config(page_title="Stock Dashboard", layout="wide")

st.title("📊 Stock Analysis Dashboard")

# ----------------------
# Select Stock
# ----------------------
symbol = st.selectbox("Select Stock", ["AAPL"])

# ----------------------
# Load Data
# ----------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/AAPL_processed.csv", index_col=0)
    return df

df = load_data()

# ----------------------
# Show Raw Data
# ----------------------
st.subheader("📄 Raw Data")
st.dataframe(df.tail())

# ----------------------
# KPI Section
# ----------------------
st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Last Price", round(df["close"].iloc[-1], 2))
col2.metric("Average Volume", int(df["volume"].mean()))
col3.metric("Volatility", round(df["volatility"].iloc[-1], 4))

# ----------------------
# Price Chart
# ----------------------
st.subheader("📈 Price & Moving Averages")

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(df.index, df["close"], label="Close", linewidth=2)
ax.plot(df.index, df["ma_5"], label="MA 5", linestyle="--")
ax.plot(df.index, df["ma_10"], label="MA 10", linestyle="--")
ax.plot(df.index, df["ma_20"], label="MA 20", linestyle="--")

ax.set_title(f"{symbol} Price Chart")
ax.legend()
plt.xticks(rotation=45)

st.pyplot(fig)

# ----------------------
# Trading Signals
# ----------------------
if "signal" in df.columns:
    st.subheader("📊 Trading Signals")

    buy = df[df["signal"] == 1]
    sell = df[df["signal"] == -1]

    fig2, ax2 = plt.subplots(figsize=(12, 5))

    ax2.plot(df.index, df["close"], label="Close")
    ax2.scatter(buy.index, buy["close"], label="Buy", marker="^")
    ax2.scatter(sell.index, sell["close"], label="Sell", marker="v")

    ax2.legend()
    plt.xticks(rotation=45)

    st.pyplot(fig2)

# ----------------------
# Correlation Heatmap
# ----------------------
st.subheader("🔥 Correlation Heatmap")

corr = df.corr()

fig3, ax3 = plt.subplots(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax3)

st.pyplot(fig3)