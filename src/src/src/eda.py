import pandas as pd
import matplotlib.pyplot as plt
import os


def run_eda():
    """
    Exploratory Data Analysis (EDA) for TCS stock data
    - Missing value analysis
    - Price distribution
    - Outlier detection using boxplot
    - Price trend over time
    """

    # Create plots directory
    os.makedirs("results/plots", exist_ok=True)

    # Load raw data
    df = pd.read_csv("data/raw/TCS_raw.csv")
    # Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Moving Averages
df["MA20"] = df["Close"].rolling(window=20).mean()
df["MA50"] = df["Close"].rolling(window=50).mean()


    # -----------------------------
    # 1. Missing Value Analysis
    # -----------------------------
    missing = df.isnull().sum()

    plt.figure(figsize=(8, 4))
    missing.plot(kind="bar")
    plt.title("Missing Values per Column")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("results/plots/missing_values.png")
    plt.close()

    # -----------------------------
    # 2. Price Distribution
    # -----------------------------
    plt.figure(figsize=(8, 4))
    plt.hist(df["Close"], bins=50)
    plt.title("TCS Close Price Distribution")
    plt.xlabel("Price")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("results/plots/price_distribution.png")
    plt.close()

    # -----------------------------
    # 3. Boxplot (Outlier Detection)
    # -----------------------------
    plt.figure(figsize=(6, 4))
    plt.boxplot(df["Close"], vert=False)
    plt.title("Boxplot of TCS Close Price")
    plt.tight_layout()
    plt.savefig("results/plots/price_boxplot.png")
    plt.close()

    # -----------------------------
    # 4. Price Trend Over Time
    # -----------------------------
    df["Date"] = pd.to_datetime(df["Date"])

    plt.figure(figsize=(10, 4))
    plt.plot(df["Date"], df["Close"], label="Close Price")
    plt.plot(df["Date"], df["MA20"], label="20-day MA")
    plt.plot(df["Date"], df["MA50"], label="50-day MA")
    plt.legend()

    plt.title("TCS Stock Price Trend (5 Years)")
    plt.xlabel("Date")
    plt.ylabel("Close Price")
    plt.tight_layout()
    plt.savefig("results/plots/price_trend.png")
    plt.close()

    print("EDA completed. Plots saved in results/plots/")


if __name__ == "__main__":
    run_eda()

