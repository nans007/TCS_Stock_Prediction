import pandas as pd
import matplotlib.pyplot as plt
import os

def run_eda():
    os.makedirs("results/plots", exist_ok=True)

    df = pd.read_csv("data/raw/TCS_raw.csv")

    # Ensure correct dtypes
    df["Date"] = pd.to_datetime(df["Date"])
    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")

    # Drop rows where Close could not be converted
    df = df.dropna(subset=["Close"])

    # Missing values
    missing = df.isnull().sum()
    plt.figure()
    missing.plot(kind="bar")
    plt.savefig("results/plots/missing_values.png")
    plt.close()

    # Boxplot (SAFE)
    plt.figure()
    plt.boxplot(df["Close"].values.astype(float), vert=False)
    plt.savefig("results/plots/price_boxplot.png")
    plt.close()

    # Price trend
    plt.figure()
    plt.plot(df["Date"], df["Close"])
    plt.savefig("results/plots/price_trend.png")
    plt.close()

    print("EDA completed")

if __name__ == "__main__":
    run_eda()


