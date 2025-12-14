import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import os

def preprocess_tcs_data():
    """
    Advanced preprocessing pipeline:
    - Missing value analysis
    - Visualization of missing values
    - Duplicate removal
    - Feature engineering
    - Normalization
    """

    # Create plots directory if not exists
    os.makedirs("results/plots", exist_ok=True)

    # Step 1: Load raw data
    df = pd.read_csv("data/raw/TCS_raw.csv")

    # Step 2: Select required columns
    df = df[['Date', 'Close']]
    df.columns = ['date', 'price']

    # Step 3: Convert date column
    df['date'] = pd.to_datetime(df['date'])

    # -------------------------------
    # MISSING VALUE ANALYSIS
    # -------------------------------

    missing_counts = df.isnull().sum()

    print("Missing values per column:")
    print(missing_counts)

    # Step 4: Visualize missing values
    plt.figure(figsize=(6,4))
    missing_counts.plot(kind='bar')
    plt.title("Missing Values Before Cleaning")
    plt.ylabel("Count")
    plt.savefig("results/plots/missing_values_before.png")
    plt.close()

    # Step 5: Handle missing values
    df.fillna(method='ffill', inplace=True)

    # -------------------------------
    # DUPLICATE CHECK
    # -------------------------------

    duplicates = df.duplicated().sum()
    print(f"Duplicate rows found: {duplicates}")

    df.drop_duplicates(inplace=True)

    # -------------------------------
    # FEATURE ENGINEERING
    # -------------------------------

    df['returns'] = df['price'].pct_change()
    df.dropna(inplace=True)

    # -------------------------------
    # NORMALIZATION (DATA PREPARATION)
    # -------------------------------

    scaler = MinMaxScaler()
    df[['price_scaled']] = scaler.fit_transform(df[['price']])

    # -------------------------------
    # DISTRIBUTION VISUALIZATION
    # -------------------------------

    plt.figure(figsize=(8,4))
    plt.hist(df['price'], bins=50)
    plt.title("Price Distribution (Before Scaling)")
    plt.savefig("results/plots/price_distribution_before.png")
    plt.close()

    plt.figure(figsize=(8,4))
    plt.hist(df['price_scaled'], bins=50)
    plt.title("Price Distribution (After Scaling)")
    plt.savefig("results/plots/price_distribution_after.png")
    plt.close()

    # Step 6: Save processed data
    df.to_csv("data/processed/TCS_cleaned.csv", index=False)

    print("Preprocessing completed successfully.")
    print("Cleaned data saved to data/processed/")

if __name__ == "__main__":
    preprocess_tcs_data()


