import yfinance as yf
import pandas as pd
import os


def collect_tcs_data():
    """
    Collect last 5 years of TCS stock price data from Yahoo Finance
    and save it as raw CSV.
    """

    # Create raw data directory
    os.makedirs("data/raw", exist_ok=True)

    # TCS ticker on NSE
    ticker = "TCS.NS"

    # Download last 5 years of daily data
    df = yf.download(
        ticker,
        period="5y",
        interval="1d"
    )

    # Reset index so Date becomes a column
    df.reset_index(inplace=True)

    # Keep only required columns
    df = df[["Date", "Open", "High", "Low", "Close", "Volume"]]

    # Save raw data
    df.to_csv("data/raw/TCS_raw.csv", index=False)

    print("5 years of TCS stock data saved to data/raw/TCS_raw.csv")


if __name__ == "__main__":
    collect_tcs_data()


