
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import os

def train_model():
    """
    Train a simple linear regression model to predict
    TCS stock closing prices based on time.
    """

    # Create plots directory if not exists
    os.makedirs("results/plots", exist_ok=True)

    # Load processed data
    df = pd.read_csv("data/processed/TCS_processed.csv")

    # Convert date to datetime
    df["date"] = pd.to_datetime(df["date"])

    # Convert date to numeric (ordinal) for regression
    df["date_ordinal"] = df["date"].map(pd.Timestamp.toordinal)

    # Features and target
    X = df[["date_ordinal"]]
    y = df["price"]

    # Train-test split (no shuffle for time series)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Plot actual vs predicted
    plt.figure(figsize=(10, 4))
    plt.plot(y_test.values, label="Actual Price")
    plt.plot(y_pred, label="Predicted Price")
    plt.title("Actual vs Predicted TCS Stock Price")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.legend()
    plt.tight_layout()
    plt.savefig("results/plots/prediction_vs_actual.png")
    plt.close()

    print("Model training completed.")
    print("Prediction plot saved to results/plots/prediction_vs_actual.png")

if __name__ == "__main__":
    train_model()
