import yfinance as yf
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load TCS data (2021–2025)
data = yf.download("TCS.NS", start="2021-01-01", end="2025-12-31")
data = data[['Close']].dropna()

# Create target
data['Target'] = data['Close'].shift(-1)
data.dropna(inplace=True)

X = data[['Close']]
y = data['Target']

# Train model
lr_model = LinearRegression()
lr_model.fit(X, y)

# Predict 2026
last_price_2025 = X.iloc[-1].values.reshape(1, -1)
lr_predicted_2026 = lr_model.predict(last_price_2025)[0]
