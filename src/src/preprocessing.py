import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import os

def preprocess_tcs_data():
    """
    Preprocessing pipeline for TCS stock data:
    - Load raw data
    - Clean and convert data types
    - Handle missing values
    - Feature engineering
    - Scaling
    - Save processed data
    """

    # Create required directories
    os.makedirs("data/processed", exist_ok=True)
    os.makedirs("results/plots", exist_ok=True)

    # Load raw data
    df = pd.read_csv("data/raw/TCS_raw.csv")

    # Keep required columns
    df = df[["Date", "Close"]]
    df.columns = ["date", "price"]

    # Convert data types
    df["date"] = pd.to_datetime(df["date"])
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # Drop missing values
    df.dropna(inplace=True)

    # Sort by date
    df.sort_values("date", inplace=True)

    # Feature engineering: daily returns
    df["returns"] = df["price"].pct_change()
    df.dropna(inplace=True)

    # Scaling
    scaler = MinMaxScaler()
    df["price_scaled"] = scaler.fit_transform(df[["price"]])

    # -------------------------------
    # Visualizations
    # -------------------------------

    # Price distribution before scaling
    plt.figure(figsize=(8, 4))
    plt.hist(df["price"], bins=50)
    plt.title("Price Distribution (Before Scaling)")
    plt.xlabel("Price")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("results/plots/price_distribution_before.png")
    plt.close()

    # Price distribution after scaling
    plt.figure(figsize=(8, 4))
    plt.hist(df["price_scaled"], bins=50)
    plt.title("Price Distribution (After Scaling)")
    plt.xlabel("Scaled Price")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("results/plots/price_distribution_after.png")
    plt.close()

    # Boxplot for outlier detection
    plt.figure(figsize=(8, 4))
    plt.boxplot(df["price"].values.astype(float), vert=False)
    plt.title("Boxplot of TCS Stock Prices")
    plt.xlabel("Price")
    plt.tight_layout()
    plt.savefig("results/plots/price_boxplot.png")
    plt.close()

    # Save processed data
    df.to_csv("data/processed/TCS_processed.csv", index=False)

    print("Preprocessing completed successfully.")
    print("Processed data saved to data/processed/TCS_processed.csv")

if __name__ == "__main__":
    preprocess_tcs_data()



