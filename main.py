from src.ingestion.alpha_vantage_api import fetch_stock
from src.processing.data_cleaning import load_and_clean
from src.features.feature_engineering import create_features
from src.analysis.visualization import plot_correlation, plot_price_with_signals, plot_signals
from src.analysis.backtesting import backtest_strategy
import os

os.makedirs("data/processed", exist_ok=True)
def main():
    # 1. Data ingestion
    df_raw = fetch_stock("AAPL")

    # 2. Cleaning
    df_clean = create_features(df_raw)

    # 3. Analysis
    plot_correlation(df_clean)

    # 4. Visualiyation
    plot_price_with_signals(df_clean)

    plot_signals(df_clean)
   
    df_bt = backtest_strategy(df_clean)
    df_bt.to_csv("data/processed/backtest.csv")

    # 5. Save processed data
    df_clean.to_csv("data/processed/AAPL_processed.csv")


if __name__ == "__main__":
    main()
