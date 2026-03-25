# 📊 Stock Analysis Pipeline

A Python-based data pipeline for fetching, processing, analyzing, and backtesting stock market data using the Alpha Vantage API.

---

## 🎯 Project Goal

This project demonstrates an end-to-end data pipeline for financial data:

- Data ingestion from external API (Alpha Vantage)
- Data cleaning and preprocessing
- Feature engineering (moving averages, returns, volatility)
- Exploratory data analysis and correlation study
- Visualization of stock trends and signals
- Experimental backtesting of a simple trading strategy

---

## 🏗️ Project Structure

```
src/
├── ingestion/
├── processing/
├── features/
├── analysis/
├── strategies/
main.py
```

---

## 📊 Results

- Strong correlation observed between short-term moving average (ma_5) and closing price
- Volume shows weak negative correlation with price
- Volatility tends to increase during market downturns

### Backtesting
- Strategy based on moving average signals
- Total Return: **-14.10%**
- Sharpe Ratio: **-2.19**
- Max Drawdown: **-18.46%**
- Win Rate: **47.50%**

---

## 📈 Visualization

- Correlation heatmap
- Price chart with moving averages
- Trading signals visualization

![Correlation](assets/correlation.png)
![Price Chart](assets/price_chart.png)

---

## 🚀 How to Run

### 1. Clone repository
```bash
git clone https://github.com/AhmadJamei/stock-analysis-pipeline.git
cd stock-analysis-pipeline
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set API key
```env
ALPHA_VANTAGE_API_KEY=your_api_key_here
```

### 5. Run
```bash
python main.py
```

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit
- Alpha Vantage API

---

## 💡 Key Insights

- Short-term momentum strongly drives price (ma_5)
- Volume shows inverse relationship with price
- Volatility spikes during market downturns

## ⚡ What this project demonstrates

- End-to-end data pipeline design
- API integration
- Data preprocessing & feature engineering
- Data visualization & analysis
- Experimental quantitative strategy implementation

---
## 📌 Notes

- Data is fetched using Alpha Vantage (rate limited)
- ll processed data is stored locally
