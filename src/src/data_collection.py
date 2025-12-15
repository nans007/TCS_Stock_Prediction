import yfinance as yf
import pandas as pd
import os

def collect_tcs_data():
    """
    Collect last 5 years of TCS stock price data from Yahoo Finance
    """

    # Create raw data directory if it doesn't exist
    os.makedirs("data/raw", exist_ok=True)

    ticker = "TCS.NS"  # TCS stock on NSE

    # Download last 5 years of daily data
    df = yf.download(
        ticker,
        period="5y",
        interval="1d"
    )

   df.reset_index(inplace=True)

    # ✅ KEEP ONLY REQUIRED COLUMNS (MUST BE HERE)
    df = df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]

    df.to_csv("data/raw/TCS_raw.csv", index=False)

    print("5 years of TCS stock data saved to data/raw/TCS_raw.csv")


if __name__ == "__main__":
    collect_tcs_data()

